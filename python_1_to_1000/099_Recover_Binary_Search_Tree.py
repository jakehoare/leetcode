_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/recover-binary-search-tree/
# The values of 2 nodes of a binary search tree (BST) are swapped by mistake.
# Recover the tree without changing its structure.

# Perform an inorder traversal tracking the previous node.  The first time a non-increasing node value is found,
# store the previous node.  The second time a non-increasing node value is found, store the node.
# E.g. for 1,2,3,8,5,6,7,4,9 we store 8 and 4.
# Time - O(n)
# Space - O(n), recursion depth worst case, log n if balanced

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.swapped1 = None
        self.swapped2 = None
        self.prev = TreeNode(float('-inf'))
        self.inorder(root)
        self.swapped1.val, self.swapped2.val = self.swapped2.val, self.swapped1.val


    def inorder(self, node):
        if not node:
            return

        self.inorder(node.left)

        if node.val <= self.prev.val:
            if not self.swapped1:
                self.swapped1 = self.prev
            if self.swapped1:
                self.swapped2 = node

        self.prev = node

        self.inorder(node.right)