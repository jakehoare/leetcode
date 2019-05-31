_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# Find the minimum element.
# You may assume no duplicate exists in the array.

# If right element is less than mid element, min mist be to right of mid.  Else min mist be mid or left.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        while left < right:

            if nums[left] <= nums[right]:   # not rotated, left is min
                break

            mid = (left + right) // 2
            if nums[right] < nums[mid]:     # min must be on right of mid
                left = mid + 1
            else:                           # nums[right] > nums[mid]
                right = mid                 # min must be mid or on left
            # nums[right] != nums[mid] because loop terminated if left == right and if right == left + 1 then
            # mid == left and since nums are unique num[left] != nums[right]

        return nums[left]