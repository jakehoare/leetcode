_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/as-far-from-land-as-possible/
# Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land,
# find a water cell such that its distance to the nearest land cell is maximized and return the distance.
# The distance used in this problem is the Manhattan distance:
# the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
# If no land or water exists in the grid, return -1.

# Breadth-first search.
# Maintain a count of frontier cells to explore, initially all the land cells.
# Maintain a count of cells reached, initially all the land cells.
# For each cell of the frontier, add all neighbours to visited count and to new frontier. Set value to 1 to avoid
# repeated visits to the same cell.
# Stop when the whole grid has been counted.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        visited = 0
        frontier = {(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 1}

        visited += len(frontier)
        if not frontier or visited == rows * cols:  # all water or all land
            return -1

        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        distance = 0

        while visited < rows * cols:                # until all grid visited
            new_frontier = set()

            for r, c in frontier:
                for dr, dc in neighbours:
                    if r + dr < 0 or r + dr >= rows:
                        continue
                    if c + dc < 0 or c + dc >= cols:
                        continue
                    if grid[r + dr][c + dc] == 0:
                        visited += 1
                        grid[r + dr][c + dc] = 1
                        new_frontier.add((r + dr, c + dc))

            frontier = new_frontier
            distance += 1

        return distance
