_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/largest-number/
# Given a list of non negative integers, arrange them such that they form the largest number.
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
# Note: The result may be very large, so you need to return a string instead of an integer.

# Comparator sorts by checking which order of concatenation gives the larger result.
# Time - O(n log n)
# Space - O(n)

import functools

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):

        def comparator(x, y):   # inputs are string representations of non-negative ints
            if x+y > y+x:       # no need to convert to int because x+y and y+x are same length
                return -1       # so lexicographic string sort behaves like numeric sort
            else:
                return 1

        nums = list(map(str, nums))     # convert to strings
        nums.sort(key=functools.cmp_to_key(comparator))

        return str(int("".join(nums)))  # remove excess leading zeroes
