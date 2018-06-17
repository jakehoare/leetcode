_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/is-graph-bipartite/
# Given an undirected graph, return true if and only if it is bipartite.
# Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that
# every edge in the graph has one node in A and another node in B.
# The graph is given as follows: graph[i] is a list of indexes j for which the edge between nodes i and j exists.
# Each node is an integer between 0 and graph.length - 1.
# There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

# Set the "colour" of each node to True or False. Iterate over nodes ignoring those that have been visited before.
# Set the colour of an unvisited node arbitrarily to True and add it to queue. Queue contains all nodes whose
# neighbours still have to be explored. Explore the queue with depth-first search, popping off a node setting its
# colour opposite to parent and failing if has same colour of parent.
# Time - O(n) the number of edges
# Space - O(m) the number of nodes

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        colours = [None] * n            # initially all nodes are not coloured

        for i in range(len(graph)):

            if colours[i] is not None:
                continue

            colours[i] = True
            queue = [i]                 # coloured nodes whose edges have not been checked

            while queue:

                v = queue.pop()

                for nbor in graph[v]:

                    if colours[nbor] is None:
                        colours[nbor] = not colours[v]  # set to opposite colour of v
                        queue.append(nbor)

                    elif colours[nbor] == colours[v]:   # inconsistency, cannot create bipartite graph
                        return False

        return True