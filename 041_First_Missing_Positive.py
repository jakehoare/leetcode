_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/first-missing-positive/
# Given an unsorted integer array, find the first missing positive integer.
# e.g. given [1,2,0] return 3, and [3,4,-1,1] return 2.
# Your algorithm should run in O(n) time and uses constant space

# If an element of nums is a positive integer that could appear in nums (1 to len(nums) inclusive) and is not in
# correct place (nums[i] = i+1) then swap.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):

            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp

            i += 1

        for i, num in enumerate(nums):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
