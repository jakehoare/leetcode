_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/check-if-it-is-a-good-array/
# Given an array nums of positive integers.
# Your task is to select some subset of nums, multiply each element by an integer and add all these numbers.
# The array is said to be good if you can obtain a sum of 1 from the array by any possible subset and multiplicand.
# Return True if the array is good otherwise return False.

# If 2 numbers have a common denominator greater than 1, they can only combine to make multiples of that
# common denominator.
# Hence we iterate along the array finding the common denominator af all previous nums until it is 1.
# Time - O(n log m) for n nums of maximum value m.
# Space - O(1)

class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def calc_gcd(a, b):
            while a > 0:
                a, b = b % a, a
            return b

        gcd = nums[0]

        for num in nums:
            gcd = calc_gcd(num, gcd)
            if gcd == 1:
                return True

        return False
