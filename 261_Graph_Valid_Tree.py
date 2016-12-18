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
        if len(edges) != n-1:                       # eliminate if too many/few edges for n nodes
            return False

        adjacency = {i : [] for i in range(n)}      # list of neighbours for each node
        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)

        self.dfs(0, adjacency)
        return not adjacency

    def dfs(self, node, adjacency):
        nbors = adjacency.pop(node, [])     # returns list of nbors of node or defaults to [] if node not in dict
        for nbor in nbors:
            self.dfs(nbor, adjacency)


class Solution2(object):
    def validTree(self, n, edges):
        if len(edges) != n-1:
            return False
        parents = [-1] * n

        for a, b in edges:

            a_parent = self.find(a, parents)
            b_parent = self.find(b, parents)

            if a_parent == b_parent:
                return False
            parents[a_parent] = b_parent

        return True

    def find(self, node, parents):
        if parents[node] == -1:
            return node
        return self.find(parents[node], parents)


sol = Solution2()
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3]]
print(sol.validTree(n, edges))