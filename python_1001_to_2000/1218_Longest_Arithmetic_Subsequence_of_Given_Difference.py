_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
# Given an integer array arr and an integer difference,
# return the length of the longest subsequence in arr which is an arithmetic sequence such that
# the difference between adjacent elements in the subsequence equals difference.

# Create a map from each number in the array to the maximum length of any subsequence ending with that number.
# Iterate over the array, updating the map by extending the sequence ending with num - difference.
# If num - difference is not in the map then we start a new sequence of length 1.
# Return the greatest length.
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        num_to_length = defaultdict(int)

        for num in arr:
            num_to_length[num] = num_to_length[num - difference] + 1

        return max(num_to_length.values())
