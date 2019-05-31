_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/inorder-successor-in-bst/
# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
# If the given node has no in-order successor in the tree, return None.

# Iterate through tree, whenever we go left update the successor.
# Alternatively recursively explore right subtree if target value >= node value since successor must then be on right.
# If target value < node value and successor is not in left subtree then node is the successor.
# Time - O(n), height of tree so log n if balanced
# Space - O(1)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        succ = None

        while root:
            if p.val >= root.val:
                root = root.right
            else:
                succ = root
                root = root.left

        return succ

class Solution2(object):
    def inorderSuccessor(self, root, p):
        if not root:
            return None

        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)

        left_succ = self.inorderSuccessor(root.left, p)

        return root if not left_succ else left_succ