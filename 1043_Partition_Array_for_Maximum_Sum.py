_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/partition-array-for-maximum-sum/
# Given an integer array A, you partition the array into (contiguous) subarrays of length at most K.
# After partitioning, each subarray has their values changed to become the maximum value of that subarray.
# Return the largest sum of the given array after partitioning.

# For each index i of A, create new subarrays of lengths 1, 2... K ending with A[i]. Track the maximum value in the
# subarray and add the maximum value * subarray length to the result for A ending before the subarray.
# Time - O(nK)
# Space - O(n)

class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        results = [0]               # results[i] for array A[:i] (of length i)

        for i in range(len(A)):

            subarray_max, max_result = 0, 0

            for j in range(i, max(-1, i - K), -1):  # first element of new subarray
                subarray_max = max(subarray_max, A[j])
                max_result = max(max_result, subarray_max * (i - j + 1) + results[j])
            results.append(max_result)

        return results[-1]
