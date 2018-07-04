_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-eventual-safe-states/
# In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.
# If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.
# Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.
# More specifically, there exists a natural number K so that for any choice of where to walk,
# we must have stopped at a terminal node in less than K steps.
# Which nodes are eventually safe?  Return them as an array in sorted order.
# The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.
# The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge.

# Topological sort. Start with a list of all safe nodes without outgoing edges. For each node, remove its incoming
# edges from the outgoing edges of its neighbours. If any neighbour then has no outgoing edges, add it to the safe list.
# Alternatively DFS marking unvisied nodes as white, known safe nodes as black and visited uncertain node as grey.
# Time - O(m + n), nodes + edges are all visited once.
# Space - O(m + n)

class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        outgoing = [set(nbors) for nbors in graph]      # convert neigbours to set of O(1) lookup
        incoming = [[] for _ in range(len(graph))]      # map node to list of nodes with incoming edges

        for node, nbors in enumerate(graph):
            for nbor in nbors:
                incoming[nbor].append(node)

        safe = [node for node, nbors in enumerate(outgoing) if not nbors]   # nodes without outgoing edges

        for safe_node in safe:                          # extended during iteration, could pop or use deque

            nbors = incoming[safe_node]
            for nbor in nbors:
                outgoing[nbor].remove(safe_node)        # remove edge safe_node -> nbor
                if not outgoing[nbor]:                  # new eventually safe node
                    safe.append(nbor)

        return [node for node, nbors in enumerate(outgoing) if not nbors]   # all nodes that are now safe
