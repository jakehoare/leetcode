_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-corner-rectangles/
# Given a grid where each entry is only 0 or 1, find the number of corner rectangles.
# A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle.
# Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.

# For each row, find the set of column indices that are 1 in the grid. Then for each pair of rows, find the common
# columns and caclulate the numbe of rectangles as each uniqie pair.
# Time - O(m**2 n)
# Space - O(mn)

class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        cols_by_row = []

        for r in range(rows):
            cols_by_row.append(set((c for c in range(cols) if grid[r][c])))

        rectangles = 0

        for high_row in range(1, rows):
            for low_row in range(high_row):
                common_cols = len(cols_by_row[high_row] & cols_by_row[low_row])
                if common_cols >= 2:
                    rectangles += common_cols * (common_cols - 1) // 2

        return rectangles