_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shortest-path-visiting-all-nodes/
# An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.
# graph.length = N, and j != i is in the list graph[i] exactly once, if and only if nodes i and j are connected.
# Return the length of the shortest path that visits every node.
# You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

# Breadth-first search. States consist of (visited, node) where node is the most recent node and visited is an
# integer with a bit set for every node visited. Expand frontier by visiting all neighbours of each node of each
# state. Only consider states not visited already.
# Time - O(n * 2**n) the number of possible states, since 2**n possible values for visited and n values for node
# Space - O(n * 2**n)

class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        if len(graph) == 0 or len(graph[0]) == 0:
            return 0

        n = len(graph)
        frontier = {(1 << node, node) for node in range(n)}     # set the bit for each node
        visited = set(frontier)
        distance = 0

        while True:

            new_frontier = set()

            for bit_nodes, node in frontier:

                if bit_nodes == 2 ** n - 1:                     # all nodes visited
                    return distance

                for nbor in graph[node]:

                    new_bit_nodes = bit_nodes | 1 << nbor       # set bit for nbor
                    if (new_bit_nodes, nbor) not in visited:
                        new_frontier.add((new_bit_nodes, nbor))

            visited |= new_frontier                             # update visited
            distance += 1
            frontier = new_frontier