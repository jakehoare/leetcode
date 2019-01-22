_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/unique-paths-iii/
# On a 2-dimensional grid, there are 4 types of squares:
# 1 represents the starting square.  There is exactly one starting square.
# 2 represents the ending square.  There is exactly one ending square.
# 0 represents empty squares we can walk over.
# -1 represents obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square,
# that walk over every non-obstacle square exactly once.

# Create a set of cells to visit and identify the start and end cells.
# From the start, recursively visit all unvisited neighbours, removing the neighbour from unvisited before recusing
# and adding it back after returning.
# Bases cases are end reached with all cells visited or it is impossible to do so.
# Time - O(4**mn)
# Space - O(mn)

class Solution:
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        unvisited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start = (r, c)
                elif grid[r][c] == 2:
                    end = (r, c)
                    unvisited.add((r, c))
                elif grid[r][c] == 0:
                    unvisited.add((r, c))

        def make_paths(r, c):
            if not unvisited and (r, c) == end:     # end reached and no more cells to visit
                return 1
            if not unvisited or (r, c) == end:      # end reached with cells to visit or no more cells to visit
                return 0

            paths = 0
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nbor_r, nbor_c = r + dr, c + dc
                if (nbor_r, nbor_c) in unvisited:
                    unvisited.remove((nbor_r, nbor_c))
                    paths += make_paths(nbor_r, nbor_c)
                    unvisited.add((nbor_r, nbor_c)) # add back after exploring this path
            return paths

        return make_paths(*start)