_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimize-malware-spread-ii/
# In a network of nodes, each node i is directly connected to another node j if and only if graph[i][j] = 1.
# Some nodes initial are initially infected by malware.
# Whenever two nodes are directly connected and at least one of those two nodes is infected by malware,
# both nodes will be infected by malware.
# This spread of malware will continue until no more nodes can be infected in this manner.
# Suppose M(initial) is the final number of nodes infected with malware in the entire network,
# after the spread of malware stops.
# We will remove one node from the initial list, completely removing it and any connections from this node
# to any other node.
# Return the node that if removed, would minimize M(initial).
# If multiple nodes could be removed to minimize M(initial), return such a node with the smallest index.

# Convert the graph to an adjacency list structure, mapping each node to its neighbours.
# For each initial node, visit all possible nodes by depth-first search. The allows us to count the number of nodes
# initially infected.
# The remove each initial node in turn and count the nodes that can be infected from the remaining initial nodes.
# Time - O(n**3), where n is the number of nodes since O(n**2) to explore the graph and O(n) initial nodes.
# Space - O(n**2)

class Solution:
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        neighbours = {}                     # map node to list of neighbours
        for i, row in enumerate(graph):
            neighbours[i] = [j for j, val in enumerate(row) if val == 1 and j != i]

        def infected():                     # return number of infected nodes, starting from initial
            for node in initial:
                connected(node)
            return len(visited)

        def connected(node):                # visit all connected nodes recursively
            if node in visited:
                return
            visited.add(node)
            for nbor in neighbours[node]:
                connected(nbor)

        visited = set()
        initial_infected = infected()

        best_gain = 0                       # best reduction in infection, achieved by removing best_node
        best_node = None

        for removed in sorted(initial):     # sort so lowest index is returned first in the event of a tie

            visited = {removed}             # do not visit removed
            infected()
            gain = initial_infected - len(visited) + 1  # add one for removed node
            if gain > best_gain:
                best_gain = gain
                best_node = removed

        return best_node