_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
# Would this affect the run-time complexity? How and why?
# Write a function to determine if a given target is in the array.

# When splitting the array at mid, one side contains the rotation point. The other side must be increasing or flat.
# Rotation point side cannot be increasing, only flat or decreasing.
# Therefor if we find an increasing side we know whether to recurse on that side or the other.
# Then if either side is not flat we know it is not sorted adn the other side is, so recurse there.
# If both sides are flat we must check them both.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        return self.binary(nums, 0, len(nums)-1, target)

    def binary(self, nums, left, right, target):

        if left > right:
            return False

        mid = (left + right) // 2
        if nums[mid] == target:
            return True

        if nums[left] < nums[mid]:          # LHS is sorted
            if target < nums[mid] and target >= nums[left]:     # check target in range of both ends
                return self.binary(nums, left, mid-1, target)   # target cannot be on RHS
            return self.binary(nums, mid+1, right, target)      # target cannot be on LHS

        if nums[mid] < nums[right]:         # RHS is sorted
            if target > nums[mid] and target <= nums[right]:    # check target in range of both ends
                return self.binary(nums, mid+1, right, target)  # target cannot be on LHS
            return self.binary(nums, left, mid-1, target)       # target cannot be on RHS

        if nums[left] == nums[mid] and nums[mid] != nums[right]:    # LHS is flat and does not include target
            return self.binary(nums, mid+1, right, target)          # so check RHS
        if nums[right] == nums[mid] and nums[mid] != nums[left]:    # RHS is flat and does not include target
            return self.binary(nums, left, mid-1, target)           # so check LHS

        if self.binary(nums, left, mid-1, target):      # both sides flat, if not fount on one side check the other
            return True
        return self.binary(nums, mid+1, right, target)

