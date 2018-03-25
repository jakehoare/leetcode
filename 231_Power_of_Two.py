_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/power-of-two/
# Given an integer, write a function to determine if it is a power of two.

# n must be positive. Powers of 2 have their most significant bit set and no other bits, so there are no set bits
# in common between n and n - 1.
# Time - O(1)
# Space - O(1)

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not n & (n - 1)