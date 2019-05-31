_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-islands/
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

# If cell is '1' then set to '0' and recurse for all adjacent cells.
# Time - O(m * n)
# Space - O(1)

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    self.set_island(r, c, grid)

        return islands

    def set_island(self, row, col, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return
        if grid[row][col] != '1':
            return
        grid[row][col] = '0'
        self.set_island(row+1, col, grid)
        self.set_island(row-1, col, grid)
        self.set_island(row, col+1, grid)
        self.set_island(row, col-1, grid)
