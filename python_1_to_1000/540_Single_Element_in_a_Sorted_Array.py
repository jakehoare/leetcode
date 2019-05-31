_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/single-element-in-a-sorted-array/
# Given a sorted array consisting of only integers where every element appears twice except for one element which
# appears once. Find this single element that appears only once.

# Binary search of even indices. Find first even index whose next number is different or missing.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1      # len(nums) - 1 is always even

        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:                # take lower even index
                mid -= 1

            if mid + 1 == len(nums) or nums[mid + 1] != nums[mid]:
                right = mid
            else:
                left = mid + 2

        return nums[left]
