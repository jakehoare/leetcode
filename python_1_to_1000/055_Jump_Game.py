_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/jump-game/
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.

# Record the maximum index that can be reached. Initially this is index 0.
# Iterate through nums, returning False an index cannot be reached.
# Else update the maximum index with the current index + its value (the maximum jump).
# Time - O(n)
# Space - O(1)

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_index = 0

        for i, num in enumerate(nums):
            if i > max_index:
                return False
            max_index = max(max_index, i + num)

        return True
