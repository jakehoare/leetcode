_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/all-paths-from-source-to-target/
# Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1
# and return them in any order.
# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for
# which the edge (i, j) exists.

# Breadth-first search. For each partial path, extend to all neighbours of the last node. If the last node is the
# destination add a copy of path to results, else add to new partial paths.
# Time - O(n**2 * n**n) max path of length n, upper limit of n**n paths
# Space - O(n * n**n)

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        paths, results = [[0]], []      # initial partial path of [0]

        while paths:

            new_paths = []

            for path in paths:
                for next_node in graph[path[-1]]:
                    destination = results if next_node == len(graph) - 1 else new_paths
                    destination.append(path[:] + [next_node])

            paths = new_paths

        return results
