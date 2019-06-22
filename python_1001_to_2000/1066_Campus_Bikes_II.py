_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/campus-bikes-ii/
# On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M.
# Each worker and bike is a 2D coordinate on this grid.
# We assign one unique bike to each worker so that the sum of the Manhattan distances between each worker
# and their assigned bike is minimized.
# The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.
# Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.

# Maintain a heap of the smallest total distance for each number of workers and some set of used bikes.
# Workers are allocated to bikes in their order in the initial list.
# The set of used bikes ir represented by an integer with a set bit indicating bikes that are used.
# Until all workers have a bike, pop the smallest distance and allocate all available (unused) bikes to the next worker.
# Do not repeat cases where the same bikes are allocated.
# Time - O(X log X) where X = b! / (b - w)!.
# Space - O(b! / (b - w)!), the number of ways to choose w from b.

import heapq

class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        distance = []
        for worker in workers:
            distance.append([])
            for bike in bikes:
                distance[-1].append(abs(worker[0] - bike[0]) + abs(worker[1] - bike[1]))

        heap = [(0, 0, 0)]      # heap of (total distance, used bike flags, workers with bikes)
        heapq.heapify(heap)
        seen = set()

        while True:
            dist, used, count = heapq.heappop(heap)
            if count == len(workers):
                return dist
            if used in seen:
                continue
            seen.add(used)

            for i in range(len(bikes)):
                if not used & (1 << i):
                    heapq.heappush(heap, (dist + distance[count][i], used | (1 << i), count + 1))
