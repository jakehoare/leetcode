_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
# Given an array nums of integers, return how many of them contain an even number of digits.

# Convert each num to string and check if length is divisible by 2.
# Time - O(n log k) for k numbers of max value k
# Space - O(log k)

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(len(str(num)) % 2 == 0 for num in nums)
