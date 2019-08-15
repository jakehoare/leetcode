_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/largest-unique-number/
# Given an array of integers A, return the largest integer that only occurs once.
# If no integer occurs once, return -1.

# Count the frequency of each number and return the maximum of numbers with a count of 1.
# Time - O(n)
# Space - O(n)

from collections import Counter

class Solution(object):
    def largestUniqueNumber(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        freq = Counter(A)
        unique = [key for key, val in freq.items() if val == 1]
        if not unique:      # no number has a count of 1
            return -1
        return max(unique)
