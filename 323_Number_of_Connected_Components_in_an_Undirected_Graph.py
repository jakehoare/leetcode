_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to find the number of connected components in an undirected graph.

# Union find. Each node is initially its own parent. For each edge, find ultimate parent of each node.
# If ultimate parents are different, union the components. Collapse unnecessary links while finding parents.
# Alternatively, BFS or DFS (better with adjacency list representation).
# Time - O(m log* n) for m edges and n nodes
# Space - O(n)

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parents = [i for i in range(n)]
        components = n

        def update_parent(node):
            while node != parents[node]:
                parents[node] = parents[parents[node]]  # collapse, set parent to grandparent
                node = parents[parents[node]]           # go up to parent
            return node

        for a, b, in edges:

            a_parent = update_parent(a)
            b_parent = update_parent(b)

            if a_parent != b_parent:
                parents[a_parent] = b_parent
                components -= 1

        return components