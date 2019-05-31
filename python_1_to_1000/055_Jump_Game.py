_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/jump-game/
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.

# Use stack to record new indices that can be reached.
# Alternatively O(1) space solution is to iterate through nums, tracking the max index that can be reached
# and returning False if next index can't be reached.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = [0]
        max_reach = -1

        while stack:

            index = stack.pop()

            if index + nums[index] > max_reach:

                if index + nums[index] >= len(nums)-1:      # can reach last index
                    return True
                for i in range(index+nums[index], max_reach, -1):
                    stack.append(i)                         # push new indices to stack, highest first
                max_reach = index + nums[index]

        return False
