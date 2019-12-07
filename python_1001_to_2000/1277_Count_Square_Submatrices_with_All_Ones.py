_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

# Iterate ove the matrix apart from the first row and column.
# Update each cell to the maximum side square with this cell in the top right corner.
# The maximum side is 0 if the cell is 0,
# else we can extend the smallest side square to the left, down or down and left by 1.
# Sum the resulting matrix, since a cell with value x has square submatrices of side lengths 1, 2 ... x ending
# with the cell in the top right corner.
# Time - O(mn)
# Space - O(Tmn)

class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0])

        for r in range(1, rows):
            for c in range(1, cols):
                matrix[r][c] *= 1 + min(matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1])

        return sum(map(sum, matrix))        # map sums each row, then sum row sums

