_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/bomb-enemy/
# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum
# enemies you can kill using one bomb.  The bomb kills all the enemies in the same row and column from the planted
# point until it hits the wall since the wall is too strong to be destroyed.
# Note that you can only put the bomb at an empty cell.

# Whenever there is a wall to the left or above we have the start of a new clear row/col.  Run along the row/col until
# either end or next wall counting enemies.  At every clear space, add the current row and col enemies.
# Time - O(m * n)
# Space - O(n)

class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        max_kill_enemies, row_kill, col_kill = 0, 0, [0 for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):

                if c == 0 or grid[r][c - 1] == "W":             # wall on left
                    row_kill, i = 0, c
                    while i < cols and grid[r][i] != "W":       # go right until end or wall
                        row_kill +=  grid[r][i] == "E"          # count enemies
                        i += 1

                if r == 0 or grid[r - 1][c] == "W":             # wall above
                    col_kill[c], i = 0, r
                    while i < rows and grid[i][c] != "W":       # go down until end or wall
                        col_kill[c] +=  grid[i][c] == "E"       # count enemies
                        i += 1

                if grid[r][c] == "0":
                    max_kill_enemies = max(max_kill_enemies, row_kill + col_kill[c])

        return max_kill_enemies
