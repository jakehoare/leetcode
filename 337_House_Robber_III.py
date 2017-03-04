_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/house-robber-iii/
# The thief has found himself a new place for his thievery again. There is only one entrance to this area,
# called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief
# realized that "all houses in this place forms a binary tree". It will automatically contact the police if two
# directly-linked houses were broken into on the same night.
# Determine the maximum amount of money the thief can rob tonight without alerting the police.

# Bottom-up recursion.  For each node find the max gain with and without robbing that node. With = value of that node
# and gain from subtrees without robbing their roots.  Without = max of left subtree gain with and without robbing its
# root + same for right subtree.
# Time - O(n)
# Space - O(1)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.helper(root))

    def helper(self, node):
        if not node:
            return 0, 0

        left_with, left_without = self.helper(node.left)
        right_with, right_without = self.helper(node.right)

        max_with = node.val + left_without + right_without
        max_without = max(left_with, left_without) + max(right_with, right_without)

        return max_with, max_without