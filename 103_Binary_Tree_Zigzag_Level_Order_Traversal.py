_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Given a binary tree, return the zigzag level order traversal of its nodes' values.
# (ie, from left to right, then right to left for the next level and alternate between).

# Alternately append new nodes from left to right and right to left.
# Time - O(n)
# Space - O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        traversal = []

        level = [root]
        forward = True

        while level:

            new_level = []
            if forward:
                traversal.append([n.val for n in level])
            else:
                traversal.append([n.val for n in level[::-1]])

            for node in level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)

            level = new_level
            forward = not forward

        return traversal

