_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-closed-islands/
# Given a 2D grid consists of 0s (land) and 1s (water).
# An island is a maximal 4-directionally connected group of 0s and a closed island
# is an island totally (all left, top, right, bottom) surrounded by 1s.
# Return the number of closed islands.

# Depth first search each land square.
# Return boolean whether the island is closed or not.
# Base cases of water and off grid are True.
# Explore all neighbours recursively, setting explored land to water to avoid cycles.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        nbors = [[1, 0], [0, 1], [-1, 0], [0, - 1]]

        def closed(r, c):               # explore an island and return whether it is closed
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return True             # stop exploration if off grid or water
            if grid[r][c] == 1:
                return True

            is_closed = 0 < r < rows - 1 and 0 < c < cols - 1   # closed if not edge of grid
            grid[r][c] = 1              # set visited land to water to avoid revisiting
            for dr, dc in nbors:
                is_closed = closed(r + dr, c + dc) and is_closed    # recurse before and to ensure exploration
            return is_closed

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:     # only explore land
                    islands += int(closed(r, c))

        return islands
