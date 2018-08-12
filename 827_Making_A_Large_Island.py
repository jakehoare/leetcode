_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/making-a-large-island/
# In a 2D grid of 0s and 1s, we change at most one 0 to a 1.
# After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).

# For each cell of the grid, find the area of its island and the set of cells neighbouring the island with depth-first
# search. Map each neighbour cell to a list of areas of neighbouring islands. Find the cell with the largest sum of
# neighbouring islands.
# Time - O(mn)
# Space - O(mn)

from collections import defaultdict

class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        nbors = ((0, 1), (1, 0), (-1, 0), (0, -1))

        def island(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:    # outside grid
                return 0
            if grid[r][c] == 2:                             # already explored
                return 0
            if grid[r][c] == 0:                             # neighbour
                edge.add((r, c))
                return 0
            grid[r][c] = 2                                  # set to visited
            return 1 + sum(island(r + dr, c + dc) for dr, dc in nbors)

        cell_to_areas = defaultdict(int)                    # map each neighbour cell to list of areas of islands

        for r in range(rows):
            for c in range(cols):
                edge = set()
                area = island(r, c)
                if area != 0:
                    for cell in edge:
                        cell_to_areas[cell] += area

        if not cell_to_areas:                               # grid empty or full
            return 1 if grid[0][0] == 0 else rows * cols
        return 1 + max(areas for areas in cell_to_areas.values())
