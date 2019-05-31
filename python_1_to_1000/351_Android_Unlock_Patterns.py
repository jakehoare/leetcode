_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/android-unlock-patterns/
# Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of
# unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.
# - Each pattern must connect at least m keys and at most n keys.
# - All the keys must be distinct.
# - If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must
# have previously selected in the pattern. No jumps through non selected key is allowed.
# - The order of keys used matters.

# BFS.  For each of 3 starting positions (corner, middle edge, centre) extend all paths by all possible new digits.
# An extension is possible if the new digit has not been used before and any required intervening digits have been
# used.  Alternatively, DFS uses less memory.
# Alternatively, having worked out the result for each digit, store the results and perform a simple sum.
# Time - O(n!)
# Space - O(n!)

class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        skips = [(1, 7, 4), (1, 9, 5), (1, 3, 2), (2, 8, 5),
                 (3, 7, 5), (3, 9, 6), (4, 6, 5), (7, 9, 8)]
        jumps = {}
        for start, end, skip in skips:
            jumps[(start, end)] = skip      # to extend from start to end requires going via skip
            jumps[(end, start)] = skip

        def count_patterns(start):

            paths = [[{start}, start]]
            patterns = 1 if m == 1 else 0
            for length in range(2, n + 1):

                new_paths = []
                for visited, last in paths:

                    for extension in range(1, 10):
                        if extension in visited:    # cannot extend is already visited digit
                            continue
                        if (last, extension) in jumps and jumps[(last, extension)] not in visited:
                            continue                # cannot extend if have not visited any intervening digit
                        new_visited = set(visited)
                        new_visited.add(extension)
                        new_paths.append([new_visited, extension])

                paths = new_paths

                if length >= m:
                    patterns += len(paths)

            return patterns

        return 4 * count_patterns(1) + 4 * count_patterns(2) + count_patterns(5)    # symmetry


class Solution2(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        patterns = [0, 9, 56, 320, 1624, 7152, 26016, 72912, 140704, 140704]
        return sum(patterns[m:n+1])

