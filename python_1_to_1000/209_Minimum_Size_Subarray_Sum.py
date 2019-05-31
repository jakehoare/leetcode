_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-size-subarray-sum/
# Given an array of n positive integers and a positive integer s, find the minimal length of a
# subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Maintain a sliding window and increase the end by 1 element at every step.  Whenever the subarray sum is >= s then
# update min_length and increment the starting index until the subarray sum < s.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        subarray_sum, min_length, start = 0, len(nums) + 1, 0   # min_length len(nums)+1 indicates no subarray sum >= s

        for i in range(len(nums)):

            subarray_sum += nums[i]     # add this element to window

            while subarray_sum >= s:    # decrease window
                min_length = min(min_length, i - start + 1)
                subarray_sum -= nums[start]
                start += 1

        return 0 if min_length > len(nums) else min_length