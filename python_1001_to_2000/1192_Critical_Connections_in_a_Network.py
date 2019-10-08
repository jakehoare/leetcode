_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/critical-connections-in-a-network/
# There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network
# where connections[i] = [a, b] represents a connection between servers a and b.
# Any server can reach any other server directly or indirectly through the network.
# A critical connection is a connection that, if removed, will make some server unable to reach some other server.
# Return all critical connections in the network in any order.

# A connection is critical if and only if it is not in any cycle in the network.
# Convert the connections to an adjacency list for each node.
# Create a set of all edges (as ordered pairs of nodes).
# Set the rank of a node as its depth when it is visited, or n when all paths have been fully explored.
# Depth-first search the graph.
# Helper function returns the rank of a node if node has already been seen, else the minimum rank of any node that
# can be reached.
# For each unvisited node, set rank to depth then recurse to neighbours apart from parent.
# If any neighbour leads to a node with lower depth then we have seen that node on the current path and the edge
# between nodes is in a cycle.
# Time - O(m + n) for m edges and n nodes
# Space - O(m + n)

from collections import defaultdict

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        node_to_nbors = defaultdict(list)
        for connection in connections:
            node_to_nbors[connection[0]].append(connection[1])
            node_to_nbors[connection[1]].append(connection[0])

        connections = {tuple(sorted(connection)) for connection in connections}
        rank = [-float("inf")] * n

        def helper(node, depth):
            if rank[node] >= 0:  # visiting (0 <= rank < n), or visited (rank == n)
                return rank[node]

            rank[node] = depth  # new node on current path
            min_nbor_path_depth = n
            for nbor in node_to_nbors[node]:
                if rank[nbor] == depth - 1:  # don't go back to parent
                    continue

                nbor_path_depth = helper(nbor, depth + 1)
                if nbor_path_depth <= depth:    # edge forms a cycle
                    connections.discard(tuple(sorted((node, nbor))))
                min_nbor_path_depth = min(min_nbor_path_depth, nbor_path_depth)
            rank[node] = n      # node fully explored
            return min_nbor_path_depth

        helper(0, 0)  # start from any arbitrary node since connected graph
        return list(connections)
