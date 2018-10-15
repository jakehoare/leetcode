_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sum-of-subsequence-widths/
# Given an array of integers A, consider all non-empty subsequences of A.
# For any sequence S, let the width of S be the difference between the maximum and minimum element of S.
# Return the sum of the widths of all subsequences of A.
# As the answer may be very large, return the answer modulo 10^9 + 7.

# Sort the numbers. For each number A[i] there are 2**i subsequences where A[i] is the maximum. Add to the result the
# maximum value of all such subsequences.
# There are 2**(len(A)-1-i) subsequences where A[i] is the minimum. Subtract from the result the minimum value of all
# such subsequences. For every subsequence the maximum is added and the minimum is subtracted, resulting in the width.
# Bitwise shift is faster than pow() or the ** operator.
# Time - O(n log n)
# Space - O(1)

class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 0
        n = len(A)
        A.sort()

        for i, num in enumerate(A):
            result += (1 << i) * num
            result -= (1 << (n - 1 - i)) * num

        return result % (10 ** 9 + 7)