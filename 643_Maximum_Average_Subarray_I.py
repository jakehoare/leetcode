_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-average-subarray-i/
# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum
# average value. And you need to output the maximum average value.

# Maintain a window with the sum of k elements. Slide the sindow along nums, updating the sum and max_average.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum = sum(nums[:k])          # assumes len(nums) >= k
        max_average = window_sum / float(k)

        for i in range(len(nums) - k):
            window_sum += nums[i + k] - nums[i]
            max_average = max(max_average, window_sum / float(k))

        return max_average