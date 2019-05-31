_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
# Given the root of a binary tree, find the maximum value V for which there exists different
# nodes A and B where V = |A.val - B.val| and A is an ancestor of B.
# A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.

# Recursive helper function tracks the max and min values seen along the current path from the root.
# The max and min values are updated at each node, returning the max difference after any leaf.
# Recurse left and right with the updated max and min and return the biggest difference from either subtree.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, min_val, max_val):
            if not node:
                return max_val - min_val

            min_val = min(node.val, min_val)
            max_val = max(node.val, max_val)

            return max(helper(node.left, min_val, max_val), helper(node.right, min_val, max_val))

        return helper(root, float("inf"), float("-inf"))
