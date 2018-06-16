_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/max-area-of-island/
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected
# 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

# Iterate over grid. If cell == 1 then perform depth-first search, setting cells to zero so they are not revisited.
# Time - O(mn)
# Space - O(1), modifies input grid

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_area = 0

        def island_area(r, c):

            grid[r][c] = 0
            area = 1

            for dr, dc in neighbours:       # faster to check valid land cell before recursing
                if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] == 1:
                    area += island_area(r + dr, c + dc)

            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:     # check only occupied cells
                    max_area = max(max_area, island_area(row, col))

        return max_area