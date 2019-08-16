_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/connecting-cities-with-minimum-cost/
# There are N cities numbered from 1 to N.
# You are given connections, where each connections[i] = [city1, city2, cost]
# represents the cost to connect city1 and city2 together.
# A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.
# Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1)
# that connects those two cities together.
# The cost is the sum of the connection costs used. If the task is impossible, return -1.

# Convert connections to map from a city to a list of neighbours connected by an edge.
# Start from any city, city 1 is chosen arbitrarily.
# Add all edges from the starting city to the heap in the form (cost, neighbour).
# Repeatedly pop off the neighbour with the lowest cost.
# If neighbour  is not already connected, update the total cost and add its unconnected neighbours to the heap.
# Time - O(n log n) for n connections.
# Space - O(n)

from collections import defaultdict
import heapq

class Solution(object):
    def minimumCost(self, N, connections):
        """
        :type N: int
        :type connections: List[List[int]]
        :rtype: int
        """
        edges = defaultdict(list)
        for a, b, cost in connections:
            edges[a].append((cost, b))
            edges[b].append((cost, a))

        connected = {1}                     # set of connected cities
        connections = list(edges[1])        # unexplored edges from connected cities
        heapq.heapify(connections)
        result = 0

        while len(connected) < N:
            if not connections:
                return -1

            cost, nbor = heapq.heappop(connections)     # cheapest cost
            if nbor in connected:
                continue
            connected.add(nbor)
            result += cost
            for edge in edges[nbor]:
                if edge[1] not in connected:  # only add if not already connected
                    heapq.heappush(connections, edge)

        return result
