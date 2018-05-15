_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/hamming-distance/
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance.

# Iterate over the bits of z and y together. If least significant bits are different, increment result. Right shift
# to move to next bit until both integers are zero.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        hamming = 0

        while x or y:
            hamming += (x & 1) != (y & 1)
            x >>= 1
            y >>= 1

        return hamming