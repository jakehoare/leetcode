_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/k-similar-strings/
# Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A
# exactly K times so that the resulting string equals B.
# Given two anagrams A and B, return the smallest K for which A and B are K-similar.

# Breadth-first search. For each word in the frontier, find the index of the first letter out of place and swap it with
# all letters which should be in that place. Memoize visited words.
# Time - O(n * n!) since n! possible words of length n if letters are unique
# Space - O(n * n!)

class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        visited = set()
        k = 0
        frontier = {A}

        while True:

            if B in frontier:
                return k

            new_frontier = set()

            for word in frontier:

                if word in visited:
                    continue

                i = 0
                while word[i] == B[i]:              # find the first word[i] that is not correct
                    i += 1

                for j in range(i + 1, len(A)):

                    if word[j] != B[i]:             # reject if word[j] is not the the letter we need at word[i]
                        continue
                    swapped = word[:i] + word[j] + word[i + 1:j] + word[i] + word[j + 1:]   # swap word[i], word[j]
                    new_frontier.add(swapped)

            k += 1
            visited |= frontier                     # add old frontier to visited
            frontier = new_frontier
