_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/divide-array-into-increasing-sequences/
# Given a non-decreasing array of positive integers nums and an integer K,
# find out if this array can be divided into one or more disjoint increasing subsequences of length at least K.

# There are at most n // K subsequences for an array of length n.
# If any element occurs more frequently than the most number of subsequences then we cannot make that many increasing
# subsequences, because the element must be duplicated in at least one subsequence.
# Else we can always take elements to make increasing subsequences.
# Time - O(n)
# Space - O(n)

from collections import Counter

class Solution(object):
    def canDivideIntoSubsequences(self, nums, K):
        """
        :type nums: List[int]
        :type K: int
        :rtype: bool
        """
        return max(Counter(nums).values()) <= len(nums) // K
