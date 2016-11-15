_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/clone-graph/
# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors

# When a new node is discovered it is copied, added to mapping and to_clone.  Main while loop makes directed edges
# to neighbors.
# Time - O(m + n), edges + nodes
# Space - O(m + n)

# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return
        cloned_start = UndirectedGraphNode(node.label)
        to_clone = [node]                       # list (or set) of original nodes
        node_mapping = {node : cloned_start}    # original to cloned nodes

        while to_clone:

            node = to_clone.pop()               # node is in mapping but does not have links to neighbors
            clone_node = node_mapping[node]

            for neighbor in node.neighbors:
                if neighbor not in node_mapping:    # create copies of neighbors if not already existing
                    clone_neightbor = UndirectedGraphNode(neighbor.label)
                    node_mapping[neighbor] = clone_neightbor
                    to_clone.append(neighbor)
                else:
                    clone_neightbor = node_mapping[neighbor]

                clone_node.neighbors.append(clone_neightbor)    # directed edges from clone_node

        return cloned_start
