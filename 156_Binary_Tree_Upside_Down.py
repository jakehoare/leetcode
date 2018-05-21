_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-tree-upside-down/
# Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the
# same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned
# into left leaf nodes. Return the new root.

# Base case for recursion is a leaf node or None. Recursively process left subtree, find rightmost path, add previous
# right on left and previous root on right.
# Time - O(n)
# Space - O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or not root.left:       # if no left then no right, leaf
            return root

        new_root = self.upsideDownBinaryTree(root.left)     # recurse left
        node = new_root
        while node.right:       # traverse as far right as possible
            node = node.right

        node.left = root.right
        node.right = root
        root.left = None
        root.right = None

        return new_root