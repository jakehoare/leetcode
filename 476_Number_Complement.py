_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-complement/
# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its
# binary representation.

# Find the number with all 1s that is the same length as num. Then take the XOR to flip the bits.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1

        while i <= num:
            i <<= 1

        return (i - 1) ^ num
