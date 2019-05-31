_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/validate-binary-search-tree/
# Given a binary tree, determine if it is a valid binary search tree (BST).
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Perform an inorder traversal and check that each node is greater than the previous.  Does not work if equal nodes
# are allowed.
# Alternatively track the upper and lower bounds possible for each node, depending on parents.
# Time - O(n)
# Space - O(n), or log n if balanced

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.correct = True
        self.prev = float('-inf')
        self.inorder(root)
        return self.correct

    def inorder(self, node):
        if not node or not self.correct:    # return if already found out of order
            return

        self.inorder(node.left)

        if node.val <= self.prev:
            self.correct = False
            return          # halt exploration
        self.prev = node.val

        self.inorder(node.right)


class Solution2(object):
    def isValidBST(self, root):
        return self.valid(root, float('-inf'), float('inf'))

    def valid(self, node, lower, upper):    # node.val must be above lower and below upper
        if not node:
            return True
        if node.val <= lower or node.val >= upper:  # can be amended if equal values are allowed
            return False
        return self.valid(node.left, lower, node.val) and self.valid(node.right, node.val, upper)
