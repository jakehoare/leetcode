_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Given preorder and inorder traversal of a tree, construct the binary tree.
# You may assume that duplicates do not exist in the tree.

# Build until we reach stop value, initially None. Take first preorder as root then recurse left until inorder is
# root value. Then discard inorder and recurse right until final stop.
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
        def build(stop):

            if not inorder or inorder[-1] == stop:
                return None

            root_val = preorder.pop()
            root = TreeNode(root_val)
            root.left = build(root_val)     # build left subtree until inorder reaches root_val
            inorder.pop()                   # then discard root_val
            root.right = build(stop)        # build right subtree until inorder reaches original stop

            return root

        preorder.reverse()      # reverse so we can pop in O(1) time
        inorder.reverse()
        return build(None)