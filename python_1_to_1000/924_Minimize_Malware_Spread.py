_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimize-malware-spread/
# In a network of nodes, each node i is directly connected to another node j if and only if graph[i][j] = 1.
# Some nodes initial are initially infected by malware.
# Whenever two nodes are directly connected and at least one of those two nodes is infected by malware,
# both nodes will be infected by malware.
# This spread of malware will continue until no more nodes can be infected in this manner.
# Suppose M(initial) is the final number of nodes infected with malware in the entire network,
# after the spread of malware stops.
# We will remove one node from the initial list.
# Return the node that if removed, would minimize M(initial).
# If multiple nodes could be removed to minimize M(initial), return such a node with the smallest index.
# Note that if a node was removed from the initial list of infected nodes, it may still be infected later as
# a result of the malware spread.

# For each node, find all connected nodes. If there is only one initially infected node in the connected group, if it
# was not infected it would improve overall the infection by the count of the group.
# Find the group of each node, ignoring nodes that already have groups.
# If every group has more than one initially infected node, return the node with the lowest index since removing
# any node cannot reduce the ultimate infection.
# Time - O(n) each node is visited and tested for membership of initial
# Space - O(n)

class Solution:
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        best_reduction = 0                  # the best reduction of infected nodes
        best_node = min(initial)            # the node that improves the infection, by default the lowest index
        initial = set(initial)              # convert to set

        def connected(node):                # recursively update group with all connected nodes
            if node in group:
                return
            group.add(node)
            [connected(nbor) for nbor, linked in enumerate(graph[node]) if linked == 1] # loop

        visited = set()                     # all nodes that are part of a group
        for node in range(len(graph)):

            if node in visited:
                continue

            group = set()
            connected(node)
            overlap = initial & group       # set of all nodes in the group that are initially infected

            if len(overlap) == 1 and len(group) > best_reduction:
                best_reduction = len(group)
                best_node = overlap.pop()

            visited |= group

        return best_node