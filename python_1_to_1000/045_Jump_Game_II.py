_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/jump-game-ii/
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
# You can assume that you can always reach the last index.

# For each index in currently accessible range, update the max_index that can be reached in one more step.
# Iterate to next range, from end of previous range to max_index.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        start, end = 0, 0   # indices in nums of current range
        max_index = 0
        steps = 1

        while True:         # will always terminate since last index is accessible
            for i in range(start, end+1):
                max_index = max(max_index, i + nums[i])
            if max_index >= len(nums)-1:
                return steps
            steps += 1
            start, end = end + 1, max_index

