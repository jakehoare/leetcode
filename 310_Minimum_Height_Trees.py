_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-height-trees/
# For a undirected graph with tree characteristics, we can choose any node as the root.
# The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called
# minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of
# their root labels.
# The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of
# undirected edges (each edge is a pair of labels).  You can assume that no duplicate edges will appear in edges.

# In each iteration of the while loop, remove all leaves (nodes with 1 neighbour).  This prunes the tree from the
# outwards resulting in either 1 or 2 nodes that are the maximum distance from any leaf.
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        connections = defaultdict(set)      # key is node, value is set of neighbouring nodes

        for a, b in edges:
            connections[a].add(b)
            connections[b].add(a)

        leaves = set(node for node in connections if len(connections[node]) == 1)

        while len(connections) > 2:
            new_leaves = set()
            for leaf in leaves:
                nbor = connections[leaf].pop()
                connections[nbor].remove(leaf)
                if len(connections[nbor]) == 1:
                    new_leaves.add(nbor)
                del connections[leaf]
            leaves = new_leaves

        return list(connections.keys())