_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/?tab=Description
# Given an array nums and a target value k, find the maximum length of a subarray that sums to k.
# If there isn't one, return 0 instead.

# Store the first index of every cumulative sum in a dictionary.  For each cumulative sum, lookup the prefix sum that
# would give a subarray ending at i and summing to k.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cumul, max_length = 0, 0
        first_index = {}

        for i, num in enumerate(nums):
            cumul += num

            if cumul == k:
                max_length = i + 1              # must be the longest
            elif cumul - k in first_index:
                max_length = max(max_length, i - first_index[cumul - k])

            if cumul not in first_index:        # add if cumul not seen before
                first_index[cumul] = i

        return max_length