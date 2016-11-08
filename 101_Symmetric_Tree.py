_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/symmetric-tree/
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# Check if left and right subtrees are both present or not, then if root values are equal.  Then recurse on their
# subtrees being mirrors - left/left of right/right and left/right of right/left
# Time - O(n)
# Space - O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, left_node, right_node):

        if not left_node and not right_node:
             return True

        if not left_node or not right_node:
             return False

        if left_node.val != right_node.val:
            return False

        return self.is_mirror(right_node.right, left_node.left) and \
               self.is_mirror(left_node.right, right_node.left)