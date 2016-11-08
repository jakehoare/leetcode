_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Given preorder and inorder traversal of a tree, construct the binary tree.
# You may assume that duplicates do not exist in the tree.

# Construct tree in preorder. Null inorder signifies preorder[0] is not part of this subtree.
# The first element of preorder is the root.  Partition the inorder list about this element.  Complete left subtree
# with all elements on left of partition, then right subtree.
# Time - O(n)
# Space - O(n)

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        preorder = deque(preorder)              # if not deque, can pop(0) from list
        return self.build(preorder, inorder)

    def build(self, preorder, inorder):

        if not inorder:     # use inorder and not preorder
            return None

        root_val = preorder.popleft()   # remove an element from deque when creating a node
        root = TreeNode(root_val)
        inorder_index = inorder.index(root_val)

        root.left = self.build(preorder, inorder[:inorder_index])
        root.right = self.build(preorder, inorder[inorder_index+1:])

        return root

