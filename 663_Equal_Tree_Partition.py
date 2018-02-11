_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/equal-tree-partition/
# Given a binary tree with n nodes, your task is to check if it's possible to partition the tree to two trees which
# have the equal sum of values after removing exactly one edge on the original tree.

# Modify the tree with bottom-up recursion so the value of each node is the sum of its original subtree. Then find a
# subtree with sum of half the total sum.
# Time - O(n)
# Space - O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def make_sum(node):
            if not node:
                return 0
            node.val += make_sum(node.left) + make_sum(node.right)
            return node.val

        tree_sum = make_sum(root)
        if tree_sum % 2 == 1:       # no partition possible
            return False

        def find_split(node):
            if not node:
                return False

            if node.left and node.left.val == tree_sum // 2:
                return True
            if node.right and node.right.val == tree_sum // 2:
                return True
            return find_split(node.left) or find_split(node.right)

        return find_split(root)