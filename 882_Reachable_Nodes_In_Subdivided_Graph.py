_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/
# Starting with an undirected graph (the "original graph") with nodes from 0 to N-1,
# subdivisions are made to some of the edges.
# The graph is given as follows: edges[k] is a list of integer pairs (i, j, n) such that (i, j) is an edge of the
# original graph, and n is the total number of new nodes on that edge.
# Then, the edge (i, j) is deleted from the original graph, n new nodes (x_1, x_2, ..., x_n) are added to the
# original graph, and n+1 new edges (i, x_1), (x_1, x_2), (x_2, x_3), ..., (x_{n-1}, x_n), (x_n, j) are added to
# the original graph.
# Now, you start at node 0 from the original graph, and in each move, you travel along one edge.
# Return how many nodes you can reach in at most M moves.

# Modified Dijkstra's algorithm. Maintain a priority queue of nodes sorted by the minimum number of steps to reach a
# that node. For each node in queue, travel along all adjacent edges visiting as many of the edges along the node as
# possible. If all edge nodes are visited, add the neighbouring node to the queue. Record the number of nodes vistied
# from both ends of each edge. Sum all real nodes visited plus the node from both sides of each edges, capped at the
# the total number of edge nodes.
# Time - O(n log n) where n is the length of edges, since each edge can be added to the heap.
# Space - O(n)

import heapq
from collections import defaultdict

class Solution(object):
    def reachableNodes(self, edges, M, N):
        """
        :type edges: List[List[int]]
        :type M: int
        :type N: int
        :rtype: int
        """
        adjacency = defaultdict(set)                    # map node to set of (nbor, number of nodes on edge)
        subdivisions = {}                               # map an edge to (number of nodes on edge, visited nodes)

        for a, b, intermediate in edges:
            subdivisions[(a, b)] = [intermediate, 0]
            subdivisions[(b, a)] = [intermediate, 0]
            adjacency[a].add((b, intermediate))
            adjacency[b].add((a, intermediate))

        queue = [(0, 0)]                                # (steps taken, node)
        visited = set()

        while queue and len(visited) < N:
            steps, node = heapq.heappop(queue)
            if node in visited:                         # already visited with lower or same steps
                continue
            visited.add(node)

            for nbor, distance in adjacency[node]:      # visit as many nodes as possible along this edge
                subdivisions[(node, nbor)][1] = min(distance, M - steps)

                if steps + distance + 1 <= M:           # visited all node on edge, add nbor to queue
                    heapq.heappush(queue, (steps + distance + 1, nbor))

        result = len(visited)                           # all nodes
        for (a, b), (distance, covered) in subdivisions.items():
            if a < b:
                result += min(distance, covered + subdivisions[(b, a)][1])  # sum edge nodes from both sides

        return result