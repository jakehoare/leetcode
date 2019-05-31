_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/random-pick-index/
# Given an array of integers with possible duplicates, randomly output the index of a given target number.
# You can assume that the given target number must exist in the array.
# The array size can be very large. Solution that uses too much extra space will not pass the judge.

# To pick, reservoir sample indices by replacing previous result with probability 1 / count of targets seen.
# Alternatively create a list of i where nums[i] == target and randomly choose and index of that list.  Only one
# random choice but more memory.
# Alternatively map each num to a list of indices which adds O(n) memory and time to intialise pick but reduces time to
# pick.
# Time - O(1) to initialise, O(n) to pick
# Space - O(1)

import random

class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = 0
        for i, num in enumerate(self.nums):
            if num == target:
                if random.randint(0, count) == 0:
                    result = i
                count += 1
        return result