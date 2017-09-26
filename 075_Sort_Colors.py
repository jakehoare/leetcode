_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sort-colors/
# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
# with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Overwrite each index with blue.  If index was red or white, add a new white and increment white pointer. If index
# was red, add a new red and increment red pointer.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        next_red, next_white = 0, 0

        for i in range(len(nums)):

            colour = nums[i]
            nums[i] = 2

            if colour < 2:
                nums[next_white] = 1
                next_white += 1

            if colour == 0:
                nums[next_red] = 0
                next_red += 1
