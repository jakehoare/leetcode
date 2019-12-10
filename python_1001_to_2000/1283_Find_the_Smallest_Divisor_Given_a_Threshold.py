_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
# Given an array of integers nums and an integer threshold,
# we will choose a positive integer divisor and divide all the array by it and sum the result of the division.
# Find the smallest divisor such that the result mentioned above is less than or equal to threshold.
# Each result of division is rounded to the nearest integer greater than or equal to that element.
# For example: 7/3 = 3 and 10/2 = 5.
# It is guaranteed that there will be an answer.

# Binary search for the divisor.
# The divisor is between 1 and max(num), inclusive.
# Search this range by guessing the mid and checking if the sum of divided num is <= threshold.
# If so, search the range from the guess and lower. Else search above the guess.
# Time - O(n log k) for n nums of max value k.
# Space - O(1)

class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def le_threshold(divisor):      # check if sum of (nums divided by divisor) is <= threshold
            return sum((num + divisor - 1) // divisor for num in nums) <= threshold

        low, high = 1, max(nums)
        while low < high:
            guess = (low + high) // 2
            if le_threshold(guess):
                high = guess
            else:
                low = guess + 1

        return low