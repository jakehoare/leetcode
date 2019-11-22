_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/tree-diameter/
# Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.
# The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.
# Each node has labels in the set {0, 1, ..., edges.length}.

# Repeatedly remove leaves (nodes with one neighbour) from the tree to find the centroid leaf or leaves.
# For each leaf removed, add new leaves if the neighbour then has only one neighbour.
# Repeat until no leaves remain (even result) or a final pair of leaves (odd result).
# Time - O(m + n)
# Space - O(m + n)

from collections import defaultdict

class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        node_to_nbors = defaultdict(set)
        for a, b in edges:
            node_to_nbors[a].add(b)
            node_to_nbors[b].add(a)

        leaves = {node for node, nbors in node_to_nbors.items() if len(nbors) == 1}

        result = 0
        while len(leaves) > 1:
            new_leaves = set()
            for leaf in leaves:
                nbor = node_to_nbors[leaf].pop()
                if nbor in leaves:      # node, nbor are final pair remaining
                    result += 1
                    break

                node_to_nbors[nbor].remove(leaf)
                if len(node_to_nbors[nbor]) == 1:
                    new_leaves.add(nbor)
            else:
                result += 2             # path extends in both directions

            leaves = new_leaves

        return result

