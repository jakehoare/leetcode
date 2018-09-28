_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/projection-area-of-3d-shapes/
# On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.
# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
# Now we view the projection of these cubes onto the xy, yz, and zx planes.
# A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane.
# Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.
# Return the total area of all three projections.

# Base area is the count of all cells with height > 0. Side areas are the sums of maximum heights by column and by
# row respectively.
# Time - O(mn)
# Space - O(m + n)

class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        row_heights, col_heights = [0] * n, [0] * n
        base_area = 0

        for row in range(n):
            for col in range(n):

                if grid[row][col] != 0:
                    base_area += 1
                row_heights[row] = max(row_heights[row], grid[row][col])
                col_heights[col] = max(col_heights[col], grid[row][col])

        return base_area + sum(row_heights) + sum(col_heights)