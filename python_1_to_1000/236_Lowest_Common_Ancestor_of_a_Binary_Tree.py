_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v
# and w as descendants (where we allow a node to be a descendant of itself).

# Recursive function return p or q if only one of those nodes is present, None if neither.
# Find LCA of p and q in and right subtrees.  If both return a value then p and q are in opposite subtrees and
# root is LCA.  Else return LCA of p and q in the subtree containing both of them.
# Time - O(n)
# Space - O(1)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if not root or p == root or q == root:      # base cases
            return root

        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        if left_lca and right_lca:
            return root
        return left_lca or right_lca