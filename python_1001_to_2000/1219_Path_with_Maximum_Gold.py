_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/path-with-maximum-gold/
# In a gold mine grid of size m * n,
# each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.
# Return the maximum amount of gold you can collect under the conditions:
# Every time you are located in a cell you will collect all the gold in that cell.
# From your position you can walk one step to the left, right, up or down.
# You can't visit the same cell more than once.
# Never visit a cell with 0 gold.
# You can start and stop collecting gold from any position in the grid that has some gold.

# For each starting position, perform depth-first search to find the maximum gold.
# DFS returns zero if a cell is out of the grid or has no gold.
# Else take the gold, set the gold in the cell to zero and recurse for all neighbours.
# Return the best result from all 4 neighbours and reset the gold in the visited cell.
# Time - O(m**2 * n**2)
# Space - O(mn)

class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def helper(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] == 0:
                return 0

            gold = best = grid[r][c]
            grid[r][c] = 0      # delete gold from visited cell
            for dr, dc in neighbours:
                best = max(best, gold + helper(r + dr, c + dc))

            grid[r][c] = gold   # reset the gold in this cell
            return best

        result = 0
        for r in range(rows):
            for c in range(cols):
                result = max(result, helper(r, c))

        return result
