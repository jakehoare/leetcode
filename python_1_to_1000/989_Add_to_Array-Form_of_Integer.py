_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/add-to-array-form-of-integer/
# For a non-negative integer X, the array-form of X is an array of its digits in left to right order.
# For example, if X = 1231, then the array form is [1,2,3,1].
# Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

# Treat K as the carry. Add carry to the least significant digit then divide by 10 to get the new carry, with the
# remainder being the new digit.
# Time - O(max(log K, n)) where n is the length of A
# Space - O(max(log K, n))

class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        for i in range(len(A) - 1, -1, -1):     # iterate from least significant digit
            A[i] += K
            K, A[i] = divmod(A[i], 10)

        return [int(c) for c in str(K)] + A if K else A     # append remaining carry if any
