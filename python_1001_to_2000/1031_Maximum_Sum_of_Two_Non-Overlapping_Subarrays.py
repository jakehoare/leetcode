_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/
# Given an array A of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous)
# subarrays, which have lengths L and M.
# For clarification, the L-length subarray could occur before or after the M-length subarray.
# Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) +
# (A[j] + A[j+1] + ... + A[j+M-1]) and either:
# 0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
# 0 <= j < j + M - 1 < i < i + L - 1 < A.length.

# Iterate over A. At each index we check the 2 cases of either L or M ending at that index.
# Update the sum of L by adding the latest element and subtracting the element leaving L.
# Update the sum of M ending immediately before L by adding and subtracting elements, then update the maximum seen
# sum of M ending before L.
# Update the result if the sum of L plus any earlier M array sum is greater than seen already.
# Check the second case by reversing the roles of L and M.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        L_sum, M_sum = sum(A[M:L + M]), sum(A[L:L + M])                     # sums of L and M ending at current index
        L_before_M_sum, M_before_L_sum = sum(A[:L]), sum(A[:M])             # sum of L ending before current M
        L_before_M_best, M_before_L_best = L_before_M_sum, M_before_L_sum   # max seen of above

        result = sum(A[:L + M])         # start from index L + M

        for i in range(L + M, len(A)):
            L_sum = L_sum + A[i] - A[i - L]
            M_before_L_sum = M_before_L_sum + A[i - L] - A[i - L - M]
            M_before_L_best = max(M_before_L_best, M_before_L_sum)
            result = max(result, L_sum + M_before_L_best)

            M_sum = M_sum + A[i] - A[i - M]
            L_before_M_sum = L_before_M_sum + A[i - M] - A[i - M - L]
            L_before_M_best = max(L_before_M_best, L_before_M_sum)
            result = max(result, M_sum + L_before_M_best)

        return result
