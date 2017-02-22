_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to find the number of connected components in an undirected graph.

# Union find. Each node is initially its own parent. For each edge find the exemplar from that connected component
# (the node with its own parent) and if different, union the components.  Union by size could improve.  Find
# collapses unnecessary links.
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

        for a, b, in edges:

            while a != parents[a]:
                a = parents[a]                      # go up to parent
                parents[a] = parents[parents[a]]    # collapse, set parent to grandparent
            a_parent = parents[a]

            while b != parents[b]:
                parents[b] = parents[parents[b]]
                b = parents[b]
            b_parent = parents[b]

            if a_parent != b_parent:
                parents[a] = b
                components -= 1

        return components