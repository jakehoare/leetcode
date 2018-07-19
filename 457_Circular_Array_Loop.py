_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/circular-array-loop/
# You are given an array of positive and negative integers. If a number n at an index is positive, then move forward
# n steps. Conversely, if it's negative (-n), move backward n steps.
# Assume the first element of the array is forward next to the last element, and the last element is backward next to
# the first element. Determine if there is a loop in this array.
# A loop starts and ends at a particular index with more than 1 element along the loop.
# The loop must be "forward" or "backward'.
# Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.
# Example 2: Given the array [-1, 2], there is no loop.
# Note: The given array is guaranteed to contain no element "0".

# For each starting num, attempt to find a sequence of n steps, which implies there must be a loop. A loop is not found
# if any step returns to the same index or moves in the opposite direction.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        for i, num in enumerate(nums):

            pos = num > 0               # direction of movements
            j = (i + num) % n           # take the first step
            steps = 1

            while steps < n and nums[j] % n != 0 and (nums[j] > 0) == pos:
                j = (j + nums[j]) % n   # take the next step
                steps += 1

            if steps == n:              # loop is found
                return True

            nums[i] = 0
            j = (i + num) % n           # set everything visited to zero to avoid repeating
            while nums[j] % n != 0 and (nums[j] > 0) == pos:
                j, nums[j] = (j + nums[j]) % n, 0

        return False
