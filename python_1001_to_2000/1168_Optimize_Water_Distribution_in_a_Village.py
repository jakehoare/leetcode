_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/optimize-water-distribution-in-a-village/
# There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.
# For each house i, we can either build a well inside it directly with cost wells[i],
# or pipe in water from another well to it.
# The costs to lay pipes between houses are given by the array pipes,
# where each pipes[i] = [house1, house2, cost] represents the cost to connect house1 and house2 together using a pipe.
# Connections are bidirectional.
# Find the minimum total cost to supply water to all houses.

# Maintain a heap of accessible sources of water, by (cost, house).
# Initial heap consists of all wells. Repeatedly use the least cost from the heap to connect an unconnected house.
# Add all pipes to neighbours to the heap. Repeat until all houses are connected.
# Time - O(m log(m + n)) for m pipes and n wells, since each pipe is added to heap of all pipes and wells.
# Space - O(m + n)

from collections import defaultdict
import heapq

class Solution(object):
    def minCostToSupplyWater(self, n, wells, pipes):
        """
        :type n: int
        :type wells: List[int]
        :type pipes: List[List[int]]
        :rtype: int
        """
        neighbours = defaultdict(list)                      # map each house to list of connected (nbor, cost)
        for house1, house2, cost in pipes:
            neighbours[house1].append((house2, cost))
            neighbours[house2].append((house1, cost))

        heap = [(cost, i + 1) for i, cost in enumerate(wells)]  # each house can be connected by a well
        heapq.heapify(heap)

        supplied = set()                                    # houses that are connected
        result = 0

        while len(supplied) < n:
            cost, house = heapq.heappop(heap)               # smallest cost connection
            if house in supplied:
                continue
            supplied.add(house)
            result += cost
            for nbor, nbor_cost in neighbours[house]:       # add all unconnected neighbours to the heap
                if nbor not in supplied:
                    heapq.heappush(heap, (nbor_cost, nbor))

        return result
