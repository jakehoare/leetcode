_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/smallest-string-with-swaps/
# You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b]
# indicates 2 indices(0-indexed) of the string.
# You can swap the characters at any pair of indices in the given pairs any number of times.
# Return the lexicographically smallest string that s can be changed to after using the swaps.

# Union-find to connect the sets of connected indices.
# Then create a mapping of each ultimate parent to all children (including the parent itself).
# For each connected group, place the sorted the characters in the sorted indices.
# Time - O(m log* m + n log n) for string length n and m pairs
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        n = len(s)
        parents = {i: i for i in range(n)}

        def find(i):
            while parents[i] != i:
                parents[i] = parents[parents[i]]    # collapse the grandparent to parent
                i = parents[i]
            return i

        for a, b in pairs:
            parents[find(a)] = find(b)

        parent_to_children = defaultdict(list)
        for i in range(n):
            parent_to_children[find(i)].append(i)

        result = [None] * n
        for children in parent_to_children.values():    # children indices are sorted
            chars = sorted(s[i] for i in children)
            for child, char in zip(children, chars):
                result[child] = char

        return "".join(result)
