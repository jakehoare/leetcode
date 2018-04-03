_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/move-zeroes/
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
# non-zero elements. For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be
# [1, 3, 12, 0, 0].
# You must do this in-place without making a copy of the array.

# Track the next index where a non-zero entry can be placed, initially zero. Iterate over nums, when a non-zero entry
# is seen, copy it to nums[i] and increment i. No action if num == 0. After iteration, replace all entries from i
# onwards with zero.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0       # next index to move a non-zero entry to

        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1

        nums[i:] = [0] * (len(nums) - i)
