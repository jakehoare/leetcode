_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
# Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to
# the sum of the values of the original tree that are greater than or equal to node.val.
# As a reminder, a binary search tree is a tree that satisfies these constraints:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Perform a reversed inorder traversal, visiting nodes from highest to lowest value.
# For each node, add its value to the running sum then update its value.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.running = 0

        def inorder(node):
            if not node:
                return
            inorder(node.right)
            self.running += node.val
            node.val = self.running
            inorder(node.left)

        inorder(root)
        return root
