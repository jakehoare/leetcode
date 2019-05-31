_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-gap/
# Given a positive integer N, find and return the longest distance between two consecutive 1's in the
# binary representation of N.
# If there aren't two consecutive 1's, return 0.

# Check each bit (from least significant to most significant). Track the index of the previous set bit and the
# maximum distance so far.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        previous, max_gap = None, 0         # index of previous 1
        i = 0                               # current index in binary representation

        while N > 0:

            if N & 1:                       # bit is set
                if previous is not None:
                    max_gap = max(max_gap, i - previous)
                previous = i

            N >>= 1                         # remove bit
            i += 1

        return max_gap