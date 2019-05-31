_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/wiggle-sort/
# Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]...

# If index is odd and not greater than or equal to previous, then swap with previous.
# If index is even and greater than or equal to previous, then swap with previous (if equal, swap has no effect).
# Time - O(n)
# Space - O(1)

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            if i%2 ^ (nums[i] >= nums[i-1]):
                nums[i], nums[i-1] = nums[i-1], nums[i]
