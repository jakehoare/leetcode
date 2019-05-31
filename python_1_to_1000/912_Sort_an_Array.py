_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sort-an-array/
# Given an array of integers nums, sort the array in ascending order.

# Use the in-built sorting function.
# Time - O(n log n)
# Space - O(n)

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(nums)
