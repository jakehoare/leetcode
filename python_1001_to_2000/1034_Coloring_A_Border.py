_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/coloring-a-border/
# Given a 2-dimensional grid of integers, each value in the grid represents the color of
# the grid square at that location.
# Two squares belong to the same connected component if and only if they have the same color and
# are next to each other in any of the 4 directions.
# The border of a connected component is all the squares in the connected component that are either
# 4-directionally adjacent to a square not in the component, or on the boundary of the grid
# (the first or last row or column).
# Given a square at location (r0, c0) in the grid and a color, color the border of the connected component of
# that square with the given color, and return the final grid.

# Depth-first search helper function return True if a cell is part of the connected component.
# If a cell is outside the grid or no the the colour of grid[r0][c0] return False.
# Recurse in all 4 directions and if not all neighbours are connected then this cell is on the border.
# Important to recurse in all directions and not check for any not connected (stopping for the first found) because
# the border colour can only be set when the cell will not be checked again.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        original = grid[r0][c0]
        rows, cols = len(grid), len(grid[0])
        connected = set()

        def dfs(r, c):
            if (r, c) in connected:             # already known to be connected, do not explore again
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != original:
                return False
            connected.add((r, c))
            if not sum(dfs(r + dr, c + dc) for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]) == 4:
                grid[r][c] = color
            return True

        dfs(r0, c0)
        return grid
