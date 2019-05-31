_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sum-of-subarray-minimums/
# Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.
# Since the answer may be large, return the answer modulo 10^9 + 7.

# Stack contains indices of elements that have not been used as the minimum of some subarray.
# Stack refers to elements in non-decreasing order. Iterate over A. While the current element of A is less than the
# top of the stack, then the top of the stack is the minimum of all subarrays bounded by the previous stack item
# and the current element. Add to the result the value of the element * number of subarrays with all possible left
# and right boundaries.
# Time - O(n)
# Space - O(n)

class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A = [float("-inf")] + A + [float("-inf")]
        result = 0
        stack = []

        for i, num in enumerate(A):

            while stack and num < A[stack[-1]]:
                j = stack.pop()
                result += A[j] * (j - stack[-1]) * (i - j)  # left boundaries of (j - top of stack), right of (i - j)

            stack.append(i)

        return result % (10 ** 9 + 7)
