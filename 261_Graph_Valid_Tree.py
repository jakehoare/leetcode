_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/graph-valid-tree/
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to check whether these edges make up a valid tree.

# Tree has the minimum number of edges to whilst still being connected.  If not n-1 edges then must be loop and/or not
# connected so not a tree.  If n-1 edges then graph is either a tree or (not connected and loop).
# Test for not connected by depth first search.  From any starting node, remove node from graph and recurse on all
# neighbours.  If any node not removed then graph is not connected so not a tree.
# Alternatively identify loops by keeping an array of the furthest node reachable from any starting node.  Union-find
# identifies connected regions.
# Time - O(n + m), nodes + edges
# Space - O(n + m)

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """

        class Solution(object):
            def validTree(self, n, edges):
                """
                :type n: int
                :type edges: List[List[int]]
                :rtype: bool
                """

                def dfs(node):                  # recursively removes nbors from mapping
                    nbors = adjacency.pop(node, [])
                    for nbor in nbors:
                        dfs(nbor)

                if len(edges) != n - 1:         # eliminate if too many/few edges for n nodes
                    return False

                adjacency = {i: [] for i in range(n)}   # list of neighbours for each node
                for a, b in edges:
                    adjacency[a].append(b)
                    adjacency[b].append(a)

                dfs(0)
                return not adjacency


class Solution2(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        def find(node):
            if parents[node] == -1:
                return node
            return find(parents[node])

        if len(edges) != n - 1:
            return False

        parents = [-1] * n

        for a, b in edges:

            a_parent = find(a)
            b_parent = find(b)

            if a_parent == b_parent:    # already have same parent before this edge
                return False
            parents[a_parent] = b_parent

        return True
