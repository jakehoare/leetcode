_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/complement-of-base-10-integer/
# Every non-negative integer N has a binary representation.
# For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.
# Note that except for N = 0, there are no leading zeroes in any binary representation.
# The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.
# For example, the complement of "101" in binary is "010" in binary.
# For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.

# Flip the sign of a bit by subtracting the bit from 1. Do this for all bits simultaneously by creating a mask with
# all bits set. The mask is 2**bit_length - 1.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:          # special case because 0 has bit_length of 1
            return 1
        return (2**N.bit_length() - 1) - N
