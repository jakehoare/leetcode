_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/trapping-rain-water-ii/
# Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map,
# compute the volume of water it is able to trap after raining.

# Simulate raising the water level from the outside of the map. Add to a heap all cells on the outer perimeter.
# Pop the lowest cell and for each neighbour not previously visited, add water to the height of the original cell
# and add neighbour to the heap.
# Time - O(mn log mn)
# Space - O(mn)

import heapq


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0

        rows, cols = len(heightMap), len(heightMap[0])
        water = 0
        q = []

        for r in range(rows):
            heapq.heappush(q, (heightMap[r][0], r, 0))
            heapq.heappush(q, (heightMap[r][cols - 1], r, cols - 1))
        for c in range(1, cols - 1):
            heapq.heappush(q, (heightMap[0][c], 0, c))
            heapq.heappush(q, (heightMap[rows - 1][c], rows - 1, c))

        visited = {(r, c) for _, r, c in q}

        while q:

            h, r, c = heapq.heappop(q)
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r1, c1 = r + dr, c + dc
                if (r1, c1) not in visited and r1 >= 0 and c1 >= 0 and r1 < rows and c1 < cols:
                    visited.add((r1, c1))
                    water += max(0, h - heightMap[r1][c1])
                    heapq.heappush(q, (max(h, heightMap[r1][c1]), r1, c1))

        return water