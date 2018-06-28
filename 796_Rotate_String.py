_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/rotate-string/
# We are given two strings, A and B. A shift of A consists of taking string A and moving the leftmost character to the
# rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A.
# Return True if and only if A can become B after some number of shifts on A.

# Rotation preserves length so if lengths differ there is no solution. If lengths are the same, there must be a copy of
# A which is a substring of the concatenation of 2 copies of B.
# Alternatively, KMP algorithm performs substring search in O(n).
# Time - O(n**2) where n == len(A) == len(B)
# Space - O(n)

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False

        return A in B + B