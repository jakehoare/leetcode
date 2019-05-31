_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/range-sum-query-2d-immutable/
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner
# (row1, col1) and lower right corner (row2, col2) where row1 ≤ row2 and col1 ≤ col2.
# You may assume that the matrix does not change.  There are many calls to sumRegion function.

# Store cumulative sums to each cell as cell value + cumulative sum to previous row + cumulative sum to previous col -
# cumulative sum to previous row and col.
# Time - O(m * n) to initialise, O(1) for sumRegion()
# Space - O(1)

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return

        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if c != 0:
                    matrix[r][c] += matrix[r][c-1]
                if r != 0:
                    matrix[r][c] += matrix[r-1][c]
                if c != 0 and r != 0:
                    matrix[r][c] -= matrix[r-1][c-1]

        self.matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        region = self.matrix[row2][col2]
        if col1 != 0:
            region -= self.matrix[row2][col1-1]
        if row1 != 0:
            region -= self.matrix[row1-1][col2]
        if row1 !=0 and col1 != 0:
            region += self.matrix[row1-1][col1-1]
        return region