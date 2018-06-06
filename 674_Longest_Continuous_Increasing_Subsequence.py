_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-continuous-increasing-subsequence/
# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

# Dynamic programming. Find longest CIS ending at each num. If non-increasing, reset current sequence length.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest, current = 0, 0

        for i, num in enumerate(nums):

            if i == 0 or num <= nums[i - 1]:
                current = 0

            current += 1
            longest = max(longest, current)

        return longest