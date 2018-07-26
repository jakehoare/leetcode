_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/burst-balloons/
# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
# You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right]
# coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.
# Find the maximum coins you can collect by bursting the balloons wisely.

# Dynamic programming.  Calculate the max coins for subarrays of increasing lengths by considering the max coins from
# all possible balloons to be burst last.  Coins gained from bursting a balloon last = coins from that balloon *
# coins from balloon before the subarray * coins from balloon after the subarray + coins from left subarray + coins
# from right subarray.
# Time - O(n**3)
# Space - O(n**2)

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = [1] + nums + [1]
        max_coins = [[0 for _ in range(n + 2)] for _ in range(n + 1)]   # row = length, col = left

        for length in range(1, n + 1):

            for left in range(1, n + 2 - length):   # consider subarrays from left to right inclusive
                right = left + length - 1

                for last in range(left, right + 1):
                    this_coins = nums[left - 1] * nums[last] * nums[right + 1]  # last balloon and neighbours
                    max_coins[length][left] = max(max_coins[length][left],
                        this_coins + max_coins[last - left][left] + max_coins[right - last][last + 1])

        return max_coins[-1][1]
