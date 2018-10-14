_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/surface-area-of-3d-shapes/
# On a N * N grid, we place some 1 * 1 * 1 cubes.
# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
# Return the total surface area of the resulting shapes.

# For each cell, add the area of top, bottom and all sides. Then subtract the side areas that are covered by
# neighbours.
# Time - O(mn)
# Space - O(1)

class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        area = 0

        for row in range(n):
            for col in range(n):

                if grid[row][col] == 0:         # ignore if no height
                    continue

                height = grid[row][col]
                area += 4 * height + 2

                if row != 0:
                    area -= min(grid[row - 1][col], height)
                if col != 0:
                    area -= min(grid[row][col - 1], height)
                if row != n - 1:
                    area -= min(grid[row + 1][col], height)
                if col != n - 1:
                    area -= min(grid[row][col + 1], height)

        return area