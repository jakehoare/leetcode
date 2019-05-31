_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/toeplitz-matrix/
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

# Iterate over matrix (in any order) apart from last row and last column. For each cell, check that it has the same
# value as the cell to the bottom right.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows - 1):
            for c in range(cols - 1):

                if matrix[r][c] != matrix[r + 1][c + 1]:
                    return False

        return True