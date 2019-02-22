_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/cousins-in-binary-tree/
# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
# Return true if and only if the nodes corresponding to the values x and y are cousins.

# Create mapping of value to node and node to parent. If both x and y are mapped to nodes, check if they have the same
# parent. If only one of x and y is mapped to a node, they are not at the same depth so are not cousins.
# Add the children of each node to the mapping.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        val_to_node = {root.val: root}  # value to nodes at current depth
        node_to_parent = {root: None}

        while True:

            x_node = val_to_node.get(x, None)
            y_node = val_to_node.get(y, None)
            if x_node is not None and y_node is not None:
                return node_to_parent[x_node] != node_to_parent[y_node]
            if x_node is not None or y_node is not None:
                return False

            new_val_to_node = {}
            for node in val_to_node.values():
                if node.left:
                    node_to_parent[node.left] = node
                    new_val_to_node[node.left.val] = node.left
                if node.right:
                    node_to_parent[node.right] = node
                    new_val_to_node[node.right.val] = node.right
            val_to_node = new_val_to_node
