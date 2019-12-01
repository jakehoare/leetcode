_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/delete-tree-nodes/
# A tree rooted at node 0 is given as follows:
# The number of nodes is nodes;
# The value of the i-th node is value[i];
# The parent of the i-th node is parent[i].
# Remove every subtree whose sum of values of nodes is zero.
# After doing so, return the number of nodes remaining in the tree.

# Map each node to its children (note this is not a binary tree, there can be any number of children).
# Recursive helper function sums all the subtrees including the node itself, and counts the nodes.
# If the sum is zero, delete the subtree by setting the node count to zero.
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def deleteTreeNodes(self, nodes, parents, values):
        """
        :type nodes: int
        :type parents: List[int]
        :type values: List[int]
        :rtype: int
        """
        node_children = defaultdict(list)
        for child, parent in enumerate(parents):
            node_children[parent].append(child)

        def helper(node):           # return (sum, node count) of subtree from node
            subtree_sum = values[node]
            subtree_count = 1

            for child in node_children[node]:   # sum and count all subtrees
                child_sum, child_count = helper(child)
                subtree_sum += child_sum
                subtree_count += child_count

            if subtree_sum == 0:    # reset count to zero since subtree is deleted
                subtree_count = 0

            return (subtree_sum, subtree_count)

        _, result = helper(0)
        return result