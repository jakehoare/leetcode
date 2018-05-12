_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/arranging-coins/
# You have a total of n coins that you want to form in a staircase, where every k-th row must have exactly k coins.
# Given n, find the total number of full staircase rows that can be formed.
# n is a non-negative integer and fits within the range of a 32-bit signed integer.

# k complete rows contain the sum form 1 to k coins = k(k + 1) / 2. Solve this quadratic polynomial for k and round down
# to nearest integer.
# Time - O(1)
# Space - O(1)

import math

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(1 + 8.0 * n) - 1) / 2