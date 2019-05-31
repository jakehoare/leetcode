_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.

# Maintain a pointer to the next index to be filled with a new number. Check every number against the previous num
# (if any) and if different, move to the next_new index.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        next_new = 0        # index where the next unique number is to be moved to

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                nums[next_new] = nums[i]
                next_new += 1

        return next_new
