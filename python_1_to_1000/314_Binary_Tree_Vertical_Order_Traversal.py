_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-tree-vertical-order-traversal/
# Given a binary tree, return the vertical order traversal of its nodes' values. (from top to bottom, column by column).
# If two nodes are in the same row and column, the order should be from left to right.

# Breadth first search tracking column number in a dictionary (since the range of columns is unknown).
# Time - O(n)
# Space - O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        vertical = defaultdict(list)
        frontier = [(root, 0)]      # (node, column) pairs

        for node, col in frontier:

            if node:
                vertical[col].append(node.val)
                frontier += [(node.left, col-1), (node.right, col+1)]
                # ok but not great to extend frontier whilst iterating over it

        return [vertical[col] for col in sorted(vertical)]




