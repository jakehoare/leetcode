_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/two-sum-less-than-k/
# Given an array A of integers and integer K,
# return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K.
# If no i, j exist satisfying this equation, return -1.

# Sort and start 2 pointers at both ends of A.
# If the sum of values at the pointers is less than K, update the best result and increment the left pointer so the
# sum of values increases.
# If the sum of values at the pointers is greater than or equal to K, decrement the right pointer so the sum of values
# decreases.
# Time - O(n log n)
# Space - O(n)

class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        result = -1
        A.sort()
        left, right = 0, len(A) - 1
        while left < right:
            if A[left] + A[right] < K:
                result = max(result, A[left] + A[right])
                left += 1
            else:
                right -= 1
        return result
