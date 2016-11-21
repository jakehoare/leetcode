_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-peak-element/
# A peak element is an element that is greater than its neighbors.
# Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# You may imagine that num[-1] = num[n] = -∞.

# If array has 3 or more elements, return mid if it is a peak else recurse on the side with a higher element.
# If array has < 3 elements, return index of greater.
# Time - O(log n)
# Space - O(n)

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1

        while left < right - 1:     # at least 3 elements

            mid = (left + right) // 2

            if nums[mid] >= nums[mid+1] and nums[mid] >= nums[mid-1]:
                return mid
            if nums[mid+1] > nums[mid]:     # RHS is higher (LHS could be also but arbitrarily choose RHS)
                left = mid + 1
            else:                           # LHS must be higher if RHS is not
                right = mid - 1

        if nums[left] >= nums[right]:
            return left
        return right