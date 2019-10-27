_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/unique-number-of-occurrences/
# Given an array of integers arr, write a function that returns true if and only if the number of
# occurrences of each value in the array is unique.

# Count the occurrences of each value and check whether the set of counts is the same size as the number of counts,
# i.e. no count is duplicated.
# Time - O(n)
# Space - O(n)

from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counts = Counter(arr)
        return len(set(counts.values())) == len(counts.values())
