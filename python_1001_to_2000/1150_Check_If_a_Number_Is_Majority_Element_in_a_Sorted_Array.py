_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/
# Given an array nums sorted in non-decreasing order, and a number target,
# return True if and only if target is a majority element.
# A majority element is an element that appears more than N/2 times in an array of length N.

# Use binary search to find the first instance of target in nums.
# If target is not in nums, return False.
# Check if
# Time - O(log n)
# Space - O(1)

import bisect

class Solution(object):
    def isMajorityElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        i = bisect.bisect_left(nums, target)
        if i == n or nums[i] != target:
            return False

        return nums[(i + n // 2) % n] == target
