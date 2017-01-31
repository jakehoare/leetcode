_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/range-sum-query-2d-mutable/
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner
# (row1, col1) and lower right corner (row2, col2).
# You may assume the number of calls to update and sumRegion function is distributed evenly.
# You may assume that row1 ≤ row2 and col1 ≤ col2.

# Store the cumulative sums for each row.  To sumRegion, sum the difference between the sum to the last and first col
# over each row.  To update, add the difference to the cumulative sum of that row for each later column.
# Time - O(mn) to initialise, O(n) to update, O(m) to sumRegion
# Space - O(mn)

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return
        rows, self.cols = len(matrix), len(matrix[0])
        self.row_sums = []
        for r in range(rows):
            self.row_sums.append([matrix[r][0]])
            for c in range(1, self.cols):
                self.row_sums[-1].append(self.row_sums[-1][-1] + matrix[r][c])
        self.matrix = matrix


    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff = val - self.matrix[row][col]
        for c in range(col, self.cols):
            self.row_sums[row][c] += diff
        self.matrix[row][col] = val


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum_region = 0
        for r in range(row1, row2+1):
            sum_region += self.row_sums[r][col2]
            if col1 != 0:
                sum_region -= self.row_sums[r][col1-1]
        return sum_region