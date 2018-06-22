_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-pivot-index/
# Given an array of integers nums, write a method that returns the "pivot" index of this array.
# We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of
# the numbers to the right of the index.
# If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most
# pivot index.

# Iterate over nums, maintaining sums of left and right sides relative to pivot. Remove num from right, then check
# whether sides have equal sums, then add num to left.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, sum(nums)          # sums of left and right arrays relative to pivot

        for i, num in enumerate(nums):

            right -= num

            if left == right:
                return i

            left += num                     # doing this last handles i == 0 better than adding previous before check

        return -1