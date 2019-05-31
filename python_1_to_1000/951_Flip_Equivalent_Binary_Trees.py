_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/flip-equivalent-binary-trees/
# For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right
# child subtrees.
# A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of
# flip operations.
# Write a function that determines whether two binary trees are flip equivalent.
# The trees are given by root nodes root1 and root2.

# Base cases are when at least one root is None. Else root values must be the same. Then recursively check whether
# the subtrees are flip equivalent either with or without swapping right and left.
# Time - O(n)
# Space - O(n)

class Solution:
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2:     # equivalent because both empty
            return True
        if not root1 or not root2:      # only one empty
            return False

        if root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) \
               or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))