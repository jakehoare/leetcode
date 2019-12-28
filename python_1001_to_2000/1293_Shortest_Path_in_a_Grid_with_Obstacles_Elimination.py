_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle).
# In one step, you can move up, down, left or right from and to an empty cell.
# Return the minimum number of steps to walk from the upper left corner (0, 0) to
# the lower right corner (m-1, n-1) given that you can eliminate at most k obstacles.
# If it is not possible to find such walk return -1.

# A-star search with heuristic of Manhattan distance.
# Repeatedly visit the state with the lowest heuristic + steps taken, ties broken by most remaining eliminations.
# Do not revisit the same cell with the same or fewer eliminations.
# Time - O(mnk log mnk) for grid of size mn each cell may be visited k times.
# Space - O(mnk)

import heapq

class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])

        def heuristic(r, c):
            return abs(rows - 1 - r) + abs(cols - 1 - c)

        queue = [(heuristic(0, 0), -k + grid[0][0], 0, 0, 0)]  # h + steps, neg_elims, steps, r, c

        visited = {}  # map cell to most eliminations remaining when cell visited

        while queue:
            _, neg_elims, steps, r, c = heapq.heappop(queue)

            if neg_elims > 0:           # too many eliminations used
                continue
            if r == rows - 1 and c == cols - 1:
                return steps

            if (r, c) in visited and neg_elims >= visited[(r, c)]:  # have visited with same or more eliminations
                continue
            visited[(r, c)] = neg_elims

            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                r2, c2 = r + dr, c + dc
                if r2 < 0 or r2 >= rows or c2 < 0 or c2 >= cols:
                    continue
                heapq.heappush(queue, (heuristic(r2, c2) + steps + 1, neg_elims + grid[r2][c2], steps + 1, r2, c2))

        return -1
