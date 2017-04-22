_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shuffle-an-array/
# Shuffle a set of numbers without duplicates.

# Copy original array and swap each entry with entry in a random position.
# Time - O(n)
# Space - O(n)

import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type size: int
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        result = self.nums[:]
        for i in range(len(result)):
            swap = random.randint(i, len(result) - 1)
            result[i], result[swap] = result[swap], result[i]
        return result