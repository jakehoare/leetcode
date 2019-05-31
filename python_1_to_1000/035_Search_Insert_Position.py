_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/search-insert-position/
# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.

# Iterative binary search until left > right or left or right move outside array.
# Return left (the greater index), which would be the new index of inserted entry (could be len(nums) but not -1).
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)

        while left <= right and left < len(nums) and right >= 0:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return left