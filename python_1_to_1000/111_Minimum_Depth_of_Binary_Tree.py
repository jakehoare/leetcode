_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# If either subtrees is not present, return 1 + minDepth of existing subtree.  If both (or neither) subtrees, return
# 1 + min of subtree minDepths
# Time - O(n)
# Space - O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        l = self.minDepth(root.left)
        r = self.minDepth(root.right)

        if not l or not r:
            return 1 + l + r

        return 1 + min(l, r)
