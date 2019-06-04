_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/campus-bikes/
# On a campus represented as a 2D grid, there are N workers and M bikes,
# with N <= M. Each worker and bike is a 2D coordinate on this grid.
# Our goal is to assign a bike to each worker.
# Among the available bikes and workers, we choose the (worker, bike) pair with the shortest Manhattan distance
# between each other, and assign the bike to that worker.
# If there are multiple (worker, bike) pairs with the same shortest Manhattan distance, we choose the pair with the
# smallest worker index; if there are multiple ways to do that, we choose the pair with the smallest bike index.
# We repeat this process until there are no available workers.
# The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.
# Return a vector ans of length N, where ans[i] is the index of the bike that the i-th worker is assigned to.

# For each worker, create a sorted list of distances to each bike.
# The elements of the list are tuples (distance, worker, bike).
# For each worker, add the tuple with the shortest distance to the heap.
# Until each worker has a bike, pop the smallest distance from the heap.
# If this bike is not used, update the result for this worker,
# else add the next closest tuple for this worker to the heap.
# Time - O(mn log mn) for m workers and n bikes.
# Space - O(mn)

import heapq

class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        distances = []      # distances[worker] is list of [distance, worker, bike] for each bike
        for i, (x, y) in enumerate(workers):
            distances.append([])
            for j, (x_b, y_b) in enumerate(bikes):
                distance = abs(x - x_b) + abs(y - y_b)
                distances[-1].append([distance, i, j])
            distances[-1].sort(reverse=True)  # reverse so we pop the smallest distance first

        result = [None] * len(workers)
        used_bikes = set()
        queue = [distances[i].pop() for i in range(len(workers))]  # smallest distance for each worker
        heapq.heapify(queue)

        while len(used_bikes) < len(workers):
            _, worker, bike = heapq.heappop(queue)
            if bike not in used_bikes:
                result[worker] = bike
                used_bikes.add(bike)
            else:
                heapq.heappush(queue, distances[worker].pop())      # bike used, add next closest bike

        return result
