_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.

# Binary search.  If one side is sorted and target is in that region then rescurse on that side or else other side.
# Time - O(log n), half of the array is eliminated for every recursion.
# Space - O(1)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.rotated_search(nums, target, 0, len(nums)-1)

    def rotated_search(self, nums, target, left, right):

        if left > right:
            return -1

        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:                                 # LHS is sorted
            if target >= nums[left] and target < nums[mid]:         # target is on LHS
                return self.rotated_search(nums, target, left, mid-1)
            return self.rotated_search(nums, target, mid+1, right)
        else:                                                       # RHS is sorted
            if target <= nums[right] and target > nums[mid]:        # target is on RHS
                return self.rotated_search(nums, target, mid+1, right)
            return self.rotated_search(nums, target, left, mid-1)


