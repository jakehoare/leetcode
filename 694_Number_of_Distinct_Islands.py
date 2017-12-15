_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-distinct-islands/
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected
# 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# Count the number of distinct islands. An island is considered to be the same as another if and only if one island
# can be translated (and not rotated or reflected) to equal the other.

# For each non-empty cell, breadth-first search for all adjacent non-empty cells. BFS by creating a queue of cells
# with positions relative to first cell, setting each cell to empty as it is found. Return tuple of relative positions
# which are counted in a set.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])

        def BFS(r, c):

            queue = [(0, 0)]  # relative to (r, c)
            for r_rel, c_rel in queue:  # queue is extended during iteration

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

                    new_r, new_c = r_rel + dr + r, c_rel + dc + c

                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 0
                        queue.append((new_r - r, new_c - c))

            return tuple(queue)

        islands = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                islands.add(BFS(r, c))

        return len(islands)