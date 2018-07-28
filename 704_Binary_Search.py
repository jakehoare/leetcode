_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-search/
# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search
# target in nums. If target exists, then return its index, otherwise return -1.

# Left and right pointers define the range of indices of nums that could contain target. Reduce target by checking
# middle element and either returning or then checking left or right side.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1      # left and right most indices of nums that could contain target

        while left <= right:

            mid = (left + right) // 2       # middle element of range

            if target == nums[mid]:
                return mid
            if target > nums[mid]:          # check right side
                left = mid + 1
            else:                           # check left side
                right = mid - 1

        return -1