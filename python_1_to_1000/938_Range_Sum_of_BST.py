_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/range-sum-of-bst/
# Given the root node of a binary search tree, return the sum of values of all nodes with value between
# L and R (inclusive).
# The binary search tree is guaranteed to have unique values.

# If the node value is more than R then recurse left only because all node values in right subtree are even greater.
# If the node value is less than L then recurse right only because all node values in left subtree are even lower.
# Else return the sum of the node value (since it is in the target range) plus the results from the left and right
# subtrees.
# Time - O(n)
# Space - O(n)

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def helper(node):

            if not node:
                return 0

            if node.val > R:
                return helper(node.left)
            if node.val < L:
                return helper(node.right)

            return node.val + helper(node.left) + helper(node.right)

        return helper(root)