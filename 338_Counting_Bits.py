_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/counting-bits/
# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's
# in their binary representation and return them as an array.

# Dynamic programming.  Number of set bits is 1 + the number of set bits in the number after removing the lowest
# set bit.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ones = [0]
        for i in range(1, num + 1):
            ones.append(1 + ones[i & (i - 1)])      # i & (i-1) removes the lowest set bit
        return ones
