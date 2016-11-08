_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/construct-binary-tree-from-postorder-and-inorder-traversal/
# Given inorder and postorder traversal of a tree, construct the binary tree.
# You may assume that duplicates do not exist in the tree.

# Construct in postorder.  Last element of postorder is root.  Partition preorder about this element.
# Build the right subtree first until postorder[0] is not in inorder.
# Time - O(n)
# Space - O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:     # no inorder signifies null tree even if postorder is not null
            return None

        inorder_index = inorder.index(postorder.pop())
        root = TreeNode(inorder[inorder_index])

        root.right = self.buildTree(inorder[inorder_index+1:], postorder)   # right first
        root.left = self.buildTree(inorder[:inorder_index], postorder)

        return root