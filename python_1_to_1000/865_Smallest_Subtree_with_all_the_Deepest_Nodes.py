_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
# Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.
# A node is deepest if it has the largest depth possible among any node in the entire tree.
# The subtree of a node is that node, plus the set of all descendants of that node.
# Return the node with the largest depth such that it contains all the deepest nodes in its subtree.

# Helper function returns the depth of the deepest node and the deepest node that is a parent of all deepest nodes.
# Recursively explore left and right subtrees. If the deepest depths are equal, the current nodeis the deepest parent
# of those deepest nodes. Else return the node from the deeper side.
# Time - O(n)
# Space - O(n)

from collections import namedtuple

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        Result = namedtuple("Result", ["node", "depth"])    # object returned by helper function

        def helper(node):

            if not node:
                return Result(None, -1)

            left_result, right_result = helper(node.left), helper(node.right)

            depth_diff = left_result.depth - right_result.depth

            if depth_diff == 0:
                return Result(node, left_result.depth + 1)

            if depth_diff > 0:
                return Result(left_result.node, left_result.depth + 1)
            return Result(right_result.node, right_result.depth + 1)

        return helper(root).node