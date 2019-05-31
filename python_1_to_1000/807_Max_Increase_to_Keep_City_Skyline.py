_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/max-increase-to-keep-city-skyline/
# In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there.
# We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for
# different buildings). Height 0 is considered to be a building as well.
# At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right,
# must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed
# by all the buildings when viewed from a distance.
# What is the maximum total sum that the height of the buildings can be increased?

# Find the maximum height in each row an each columns. For each cell in the grid, the building can be increased to the
# lower of the row and column maximum heights.
# Time - O(mn)
# Space - O(m + n)

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        row_sky = [0 for _ in range(rows)]          # max heights by row
        col_sky = [0 for _ in range(cols)]          # max heights by col

        for r in range(rows):
            for c in range(cols):
                row_sky[r] = max(row_sky[r], grid[r][c])
                col_sky[c] = max(col_sky[c], grid[r][c])

        increase = 0

        for r in range(rows):
            for c in range(cols):
                increase += min(row_sky[r], col_sky[c]) - grid[r][c]

        return increase