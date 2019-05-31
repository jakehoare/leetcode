_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Given a binary tree, return the bottom-up level order traversal of its nodes' values.
# I.e. from left to right, level by level from leaf to root.

# Perform an inorder traversal, tracking depth and appending node values to corresponding sub-list.  Reverse
# result before returning.
# Time - O(n)
# Space - O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        traversal = []
        self.inorder(root, 0, traversal)
        return traversal[::-1]

    def inorder(self, node, depth, traversal):

        if not node:
            return

        if len(traversal) == depth:
            traversal.append([])

        self.inorder(node.left, depth+1, traversal)

        traversal[depth].append(node.val)

        self.inorder(node.right, depth+1, traversal)

