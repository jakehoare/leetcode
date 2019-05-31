_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shortest-distance-from-all-buildings/
# You want to build a house on an empty land which reaches all buildings in the shortest amount of distance.
# You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:
# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
# There will be at least one building. If it is not possible to build such house, return -1.

# For each house explore all of the grid that is reachable by previous houses with BFS.  Add the distance from the
# house to a copy of the grid.  BFS is pruned by only considering cells reached by earlier houses.
# Time - O(m * n * h) where h is the number of houses
# Space - O(m * n)

from copy import deepcopy

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        house = 0                       # number of the current house performing BFS
        distances = deepcopy(grid)      # sum of distances from all explored houses to each point

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] != 1:     # not a house
                    continue
                q = [(row, col)]            # frontier of all cells to be explored
                house_dist = 1

                while q:
                    new_q = []
                    for r, c in q:
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            # if within grid and has been explored by all previous houses
                            if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] == -house:
                                grid[r + dr][c + dc] -= 1           # signify that another house has reached here
                                new_q.append((r + dr, c + dc))      # add to list to explore
                                distances[r + dr][c + dc] += house_dist     # add to cumulative distances

                    house_dist += 1
                    q = new_q

                house += 1

        # reachable are those distances of cells reached by all houses
        reachable = [distances[r][c] for r in range(rows) for c in range(cols) if grid[r][c] == -house]
        return -1 if not reachable else min(reachable)
