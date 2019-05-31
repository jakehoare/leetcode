_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sum-of-distances-in-tree/
# An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.
# The ith edge connects nodes edges[i][0] and edges[i][1] together.
# Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.

# Create map from node to neighbours. Depth-first search from node 0, counting the number of nodes in each subtree and
# calculating the distance from each root to all nodes in subtree. The distances from node 0 is then correct.
# Depth-first search again, calculating the distance to every child as the parent distance minus 1 for every node in
# the subtree (which is now closer), plus 1 for every node not in subtree (which is now further away).
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        neighbours = defaultdict(set)               # map node to set of neighbours
        for a, b in edges:
            neighbours[a].add(b)
            neighbours[b].add(a)

        subtree_counts = [1] * N                    # number of nodes in subtree with node i as roor
        distances = [0] * N

        def subtree_distances(node, parent):
            for child in neighbours[node]:
                if child != parent:                 # graph is undirected, do not go back to parent
                    subtree_distances(child, node)
                    subtree_counts[node] += subtree_counts[child]
                    distances[node] += distances[child] + subtree_counts[child] # each node in subtree is 1 unit further

        def update_distances(node, parent):
            for child in neighbours[node]:
                if child != parent:
                    distances[child] = distances[node] - subtree_counts[child] + (N - subtree_counts[child])
                    update_distances(child, node)

        subtree_distances(0, None)
        update_distances(0, None)
        return distances