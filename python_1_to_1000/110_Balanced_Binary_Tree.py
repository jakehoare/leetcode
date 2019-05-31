_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/balanced-binary-tree/
# Given a binary tree, determine if it is height-balanced.
# A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node
# never differ by more than 1.

# Helper function balanced returns the depth of the root if the tree is balance or else -1 if not balanced.
# A tree is not balance if either left or right subtree is not balanced, or the difference in left and right subtree
# depths is greater than 1.
# Time - O(n), visit all nodes
# Space - O(n)

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def balanced(node):

            if not node:
                return 0

            left_depth = balanced(node.left)
            right_depth = balanced(node.right)

            if left_depth == -1 or right_depth == -1:
                return -1
            if abs(left_depth - right_depth) > 1:
                return -1

            return 1 + max(left_depth, right_depth)

        return balanced(root) != -1


