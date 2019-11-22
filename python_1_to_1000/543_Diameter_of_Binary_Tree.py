_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/diameter-of-binary-tree/
# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.

# Bottom up recursion.
# The longest path passing with a node as root is the longest downwards left path + longest downwards right path.
# If there is no child on right or left then the longest path on that side is zero.
# Else longest path is 1 + longest of left and right paths down from child.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0

        def helper(node):       # return longest downwards path
            if not node:
                return -1       # so leaf returns zero
            left = helper(node.left)
            right = helper(node.right)
            self.result = max(self.result, 2 + left + right)
            return max(1 + left, 1 + right)

        helper(root)        # ignore return value
        return self.result