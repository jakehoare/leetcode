_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/redundant-connection/
# In this problem, a tree is an undirected graph that is connected and has no cycles.
# The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one
# additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that
# already existed.
# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that
# represents an undirected edge connecting nodes u and v.
# Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers,
# return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same
# format, with u < v.

# Every edge of a tree connects two sets of nodes that are not otherwise connected. Find the edge that connects already
# connected nodes with union find structure.
# Find parents of both nodes of an edge. If same then there is already a path between nodes. Else connect
# the parents.
# Time - O(n log* n)
# Space - O(n)

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parents = {}

        def find_parent(n):

            if n not in parents:                        # n is a new node or ultimate parent
                return n
            parents[n] = find_parent(parents[n])        # collapse parent to be ultimate parent
            return parents[n]                           # return ultimate parent

        for a, b in edges:

            parent_a, parent_b = find_parent(a), find_parent(b)
            if parent_a == parent_b:
                return [a, b]

            parents[parent_a] = parent_b                # union join