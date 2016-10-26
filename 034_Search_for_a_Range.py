_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/search-for-a-range
# Given a sorted array of integers, find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].

# Search for target +/- 0.5 (not integer so not found) and return the index above this.
# If same index is returned for + and - 0.5 then target not found.
# Binary search could be implemented iteratively.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lower = self.binary(nums, target-0.5, 0, len(nums)-1)
        upper = self.binary(nums, target+0.5, 0, len(nums)-1)
        return [-1, -1] if lower == upper else [lower, upper-1]

    def binary(self, nums, target, left, right):
        if left > right:
            return left
        mid = (left + right) // 2
        while target > nums[mid]:
            return self.binary(nums, target, mid+1, right)
        return self.binary(nums, target, left, mid-1)
