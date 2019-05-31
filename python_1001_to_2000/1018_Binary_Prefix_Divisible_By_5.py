_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-prefix-divisible-by-5/
# Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number,
# from most-significant-bit to least-significant-bit.
# Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.

# Iterate over A. For each bit, multiply the existing num by 2 (bit shift left) and add the bit. Take modulo 5, since
# mod is preserved under multiplication and addition.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        result = []
        num = 0

        for bit in A:
            num = (num * 2 + bit) % 5
            result.append(num == 0)

        return result
