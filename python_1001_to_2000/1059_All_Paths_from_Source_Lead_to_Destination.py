_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/all-paths-from-source-lead-to-destination/
# Given the edges of a directed graph, and two nodes source and destination of this graph,
# determine whether or not all paths starting from source eventually end at destination, that is:
# At least one path exists from the source node to the destination node
# If a path exists from the source node to a node with no outgoing edges, then that node is equal to destination.
# The number of possible paths from source to destination is a finite number.
# Return true if and only if all roads from source lead to destination.

# Build a map from each node to the set of nodes connected by an edge.
# From the source node, recursively explore all neighbours adding them to the visited set and testing whether all
# paths lead to the destination. Remove nodes from visited set when returning from recursion.
# Time - O(m + n), nodes + edges
# Space - O(m + n)

from collections import defaultdict

class Solution(object):
    def leadsToDestination(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        visited = set()
        edge_dict = defaultdict(set)
        for start, end in edges:
            edge_dict[start].add(end)

        def can_reach_dest(node):
            if node == destination and len(edge_dict[node]) == 0:   # destination reached and no neighbours
                return True
            if node == destination or len(edge_dict[node]) == 0:    # destination has neighbours or terminal node
                return False                                        # that is not destination

            if node in visited:
                return False
            visited.add(node)
            result = all(can_reach_dest(nbor) for nbor in edge_dict[node])
            visited.remove(node)
            return result

        return can_reach_dest(source)
