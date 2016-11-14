_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers.

# Recursively find the sum of all paths from a node to all leaves having already seen path value of partial.
# Time - O(n)
# Space - O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, 0)

    def helper(self, node, partial):

        if not node:    # no path to leaves
            return 0

        partial = 10 * partial + node.val       # incorporate this node.val

        if not node.left and not node.right:    # base case, leaf
            return partial

        return self.helper(node.left, partial) + self.helper(node.right, partial)