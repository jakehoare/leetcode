_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/swim-in-rising-water/
# On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).
# Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another
# 4-directionally adjacent square if and only if the elevation of both squares individually are at most t.
# You can swim infinite distance in zero time. You must stay within the boundaries of the grid during your swim.
# Start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

# Maintain a priority queue of cells on edge of explored region. Pop lowest cell and update the high water mark.
# Add neighbours to frontier if not already visited. If lower cells are added to frontier they will be removed before
# any higher cells.
# Time - O(n**2 logn)
# Space - O(n**2)

import heapq

class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        shifts = ((0, 1), (0, -1), (1, 0), (-1, 0))
        frontier = [(grid[0][0], 0, 0)]         # cells not explored but on edge of explored region
        visited = {(0, 0)}                      # frontier and explored cells

        max_water = 0

        while True:

            water, r, c = heapq.heappop(frontier)   # lowest cell that is reachable

            max_water = max(max_water, water)

            if r == c == N - 1:                     # reached target
                return max_water

            for dr, dc in shifts:

                if r + dr < 0 or r + dr >= N or c + dc < 0 or c + dc >= N:
                    continue
                if (r + dr, c + dc) in visited:
                    continue
                visited.add((r + dr, c + dc))
                heapq.heappush(frontier, (grid[r + dr][c + dc], r + dr, c + dc))
