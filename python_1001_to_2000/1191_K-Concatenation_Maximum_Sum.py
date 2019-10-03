_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/k-concatenation-maximum-sum/
# Given an integer array arr and an integer k, modify the array by repeating it k times.
# For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].
# Return the maximum sub-array sum in the modified array.
# Note that the length of the sub-array can be 0 and its sum in that case is 0.
# As the answer can be very large, return the answer modulo 10^9 + 7.

# Iterate along the array, finding the maximum sum prefix and the maximum sum subarray.
# Iterate along the array in reverse, finding the maximum sum suffix.
# If k == 1, return the maximum sum subarray.
# Else we can use the maximum sum subarray or the max prefix + max suffix.
# If the array sum is positive we can insert (k - 2) copies of the whole array between suffix and prefix.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        total = sum(arr)

        max_prefix, max_end_here, max_subarray = 0, 0, 0
        cumulative = 0
        for a in arr:
            cumulative += a
            max_prefix = max(max_prefix, cumulative)
            max_end_here = max(max_end_here, 0) + a
            max_subarray = max(max_subarray, max_end_here)

        max_suffix = 0
        cumulative = 0
        for a in arr[::-1]:
            cumulative += a
            max_suffix = max(max_suffix, cumulative)

        if k == 1:
            return max_subarray % MOD
        return max(max_subarray, max_prefix + max_suffix + max(total, 0) * (k - 2)) % MOD
