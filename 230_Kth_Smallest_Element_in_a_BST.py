_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Iterative inorder traversal.
# Alternatively, recursive inorder traversal tracking remaining count with instance variable.
# Time - O(n)
# Space - O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right
            while node:
                stack.append(node)
                node = node.left

class Solution2(object):
    def kthSmallest(self, root, k):
        self.k = k              # instance variables
        self.result = None
        self.helper(root)
        return self.result

    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.result = node.val
            return
        self.helper(node.right)
