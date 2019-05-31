_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/repeated-string-match/
# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it.
# If no such solution, return -1.

# Repeat A until it is at least the length of B. If B is not a substring, then test with another copy of A added.
# More copies of A are not required because at least one copy of A will not be used.
# Time - O(n + m)
# Space - O(n + m)

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if set(B) - set(A):         # early return
            return -1

        div, mod = divmod(len(B), len(A))

        if mod != 0:
            div += 1

        for i in range(2):
            if B in A * (div + i):
                return div + i

        return -1
