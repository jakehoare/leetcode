_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/largest-number-at-least-twice-of-others/
# In a given integer array nums, there is always exactly one largest element.
# Find whether the largest element in the array is at least twice as much as every other number in the array.
# If it is, return the index of the largest element, otherwise return -1.

# Iterate over nums, tracking the index of the largest num seen and the second largest num seen.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_i = 0     # index of largest num
        second = 0      # second largest num

        for i, num in enumerate(nums[1:], 1):

            if num >= nums[first_i]:
                first_i, second = i, nums[first_i]      # update first_i and second
            elif num > second:
                second = num

        return first_i if nums[first_i] >= 2 * second else -1   # check if first is at least twice second