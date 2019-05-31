_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sparse-matrix-multiplication/
# Given two sparse matrices A and B, return the result of AB.
# You may assume that A's column number is equal to B's row number.

# When an element of A is non-zero update all elements of C using that element.  Skip if element of A is sero.
# Scales linearly with the density of A.
# Time - O(m*n*p) for A being (m by n) and B being (n by p)
# Space - O(m*p)

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        rows_A, cols_A = len(A), len(A[0])
        cols_B = len(B[0])      # rows_B = cols_A

        C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

        for r in range(rows_A):
            for c in range(cols_A):

                if A[r][c] != 0:
                    for i in range(cols_B):
                        C[r][i] += A[r][c] * B[c][i]

        return C