_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Given a binary tree, find the maximum path sum.
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in
# the tree along the parent-child connections.
# The path must contain at least one node and does not need to go through the root.

# Recursive helper function calculates max path downwards from and including any node and max path via a node or via
# any node below.
# Time - O(n)
# Space - O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[0]

    def helper(self, node):     # returns tuple of (via, down) where via is max path sum via (and including) this node
                                # or via any node below, down is max path sum downwards from this node
        if not node:
            return float('-inf'), 0     # -inf for via if no node since path must have at least one node

        left_via, left_down = self.helper(node.left)
        right_via, right_down = self.helper(node.right)

        # either use this node and go down left and/or right if positive, or best of left and right via.
        via = max(node.val + max(0, left_down) + max(0, right_down), left_via, right_via)
        # use this node and go down max of right or left if positive.
        down = node.val + max(0, left_down, right_down)

        return via, down


