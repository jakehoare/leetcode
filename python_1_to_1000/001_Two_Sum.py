_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/two-sum/
# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution.

# Maintain a mapping from each number to its index.
# Check if target - num has already been found.
# Time - O(n)
# Space - O(n) for the dictionary

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_to_index = {}           # key is number, value is index in nums

        for i, num in enumerate(nums):

            if target - num in num_to_index:
                return [num_to_index[target - num], i]

            num_to_index[num] = i

        return []   # no sum
