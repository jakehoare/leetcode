_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/island-perimeter/
# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
# and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water
# inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid
# is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

# Iterate over grid. If a cell is land, add 4 to perimeter assuming cell is surrounded by water. Then for each of lower
# and right cells that are land, decrement the perimeter by 2 (both sides of the internal edge).
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        for row in grid:                # pad with water
            row.append(0)
        grid.append([0] * (cols + 1))
        perimiter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimiter += 4
                    if grid[r + 1][c] == 1:
                        perimiter -= 2
                    if grid[r][c + 1] == 1:
                        perimiter -= 2

        return perimiter