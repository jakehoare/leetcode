_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-sum-circular-subarray/
# Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.
# Here, a circular array means the end of the array connects to the beginning of the array.
# Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.
# Also, a subarray may only include each element of the fixed buffer A at most once.
# Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with
# k1 % A.length = k2 % A.length.

# Iterate over A, finding the max and min sum subarrays that end at each index.
# The result either does not use the circularity of A, in which case it is the maximum sum subarray within A.
# Or the result is the sum of A minus the minimum sun subarray within A.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if all(num <= 0 for num in A):
            return max(A)

        overall_max, overall_min = float('-inf'), float('inf')
        max_ending_here, min_ending_here = 0, 0

        for num in A:

            max_ending_here = max(max_ending_here, 0) + num     # if previous max negative, set to zero
            min_ending_here = min(min_ending_here, 0) + num     # if previous min positive, set to zero

            overall_max = max(overall_max, max_ending_here)
            overall_min = min(overall_min, min_ending_here)

        return max(overall_max, sum(A) - overall_min)