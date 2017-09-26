_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-element/
# Given an array and a value, remove all instances of that value in place and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Maintain pointer to next index to be used for any number not equal to val.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        next_free = 0
        for i, num in enumerate(nums):
            if num != val:
                nums[next_free] = num
                next_free += 1
        return next_free
