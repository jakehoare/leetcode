_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/path-sum-ii/
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# Maintain a partial path, appending latest node and decrementing target. When path has been explored, pop node off
# partial path. Base cases are no node and leaf with remaining target of zero.
# Time - O(n log n), balanced tree has n/2 leaves and height log n
# Space - O(n log n), every path of balanced tree has correct sum

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        paths = []
        self.preorder(root, sum, [], paths)
        return paths

    def preorder(self, node, target, partial, paths):

        if not node:
            return

        target -= node.val
        partial.append(node.val)
        if target == 0 and not node.left and not node.right:
            paths.append(partial[:])

        self.preorder(node.left, target, partial, paths)
        self.preorder(node.right, target, partial, paths)

        partial.pop()