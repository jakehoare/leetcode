_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shortest-path-with-alternating-colors/
# Consider a directed graph, with nodes labelled 0, 1, ..., n-1.
# In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.
# Each [i, j] in red_edges denotes a red directed edge from node i to node j.
# Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.
# Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X
# such that the edge colors alternate along the path (or -1 if such a path doesn't exist).

# Breadth-first search the graph of (node, next colour).
# Expand all neighbours of frontier, ignoring (node, colour) seen before.
# Update result on first instance of visiting a node.
# Time - O(m + n)
# Space - O(m + n)

from collections import defaultdict

class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        red, blue = defaultdict(list), defaultdict(list)    # convert edges to maps from node to neighbours
        for start, end in red_edges:
            red[start].append(end)
        for start, end in blue_edges:
            blue[start].append(end)

        result = [-1] * n                       # default to -1
        frontier = [(0, True), (0, False)]      # list of (node, is_red) to explore
        steps = 0
        visited = set()

        while frontier:
            new_frontier = []
            for node, is_red in frontier:
                if (node, is_red) in visited:   # visited this node, colour combination already
                    continue
                visited.add((node, is_red))
                if result[node] == -1:          # first visit to this node
                    result[node] = steps

                nbors = red[node] if is_red else blue[node]
                new_frontier += [(nbor, not is_red) for nbor in nbors]

            frontier = new_frontier
            steps += 1

        return result
