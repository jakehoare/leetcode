_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/balanced-binary-tree/
# Given a binary tree, determine if it is height-balanced.
# A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Calculate the depth of each node or -1 if not balanced.  Not balanced if either subtree not balanced or difference in
# max subtree depths is more than 1.
# Time - O(n), visit all nodes
# Space - O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.balanced(root) != -1

    def balanced(self, node):

        if not node:
            return 0

        left_depth = self.balanced(node.left)
        right_depth = self.balanced(node.right)

        if left_depth == -1 or right_depth == -1:
            return False
        if abs(left_depth - right_depth) > 1:
            return False

        return 1 + max(left_depth, right_depth)

