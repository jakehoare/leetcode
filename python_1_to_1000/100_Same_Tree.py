_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/same-tree/
# Given two binary trees, write a function to check if they are equal or not.
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

# Traverse both trees, checking nodes exist in same places and values are same.  Could preorder, inorder or postorder.
# Time - O(min(m, n))
# Space - O(min(m, n)), or log is balanced

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False

        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


