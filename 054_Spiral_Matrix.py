_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/spiral-matrix/
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Use row_leg and col_leg to traxk the max number of moves before turning.  Decrease row_leg and col_leg then turning.
# Time - O(m * n)
# Space - O(1)

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        spiral = []
        row, col = 0, -1
        d_row, d_col = 0, 1     # movement direction
        row_leg, col_leg = len(matrix[0]), len(matrix)-1    # steps before change of direction
        leg_count = 0                                       # count of steps in current direction

        for _ in range(len(matrix[0]) * len(matrix)):

            row += d_row
            col += d_col
            spiral.append(matrix[row][col])
            leg_count += 1

            # change direction
            if (d_col != 0 and leg_count == row_leg) or (d_row != 0 and leg_count == col_leg):
                if d_col != 0:
                    row_leg -= 1
                else:
                    col_leg -= 1
                d_row, d_col = d_col, -d_row
                leg_count = 0

        return spiral
