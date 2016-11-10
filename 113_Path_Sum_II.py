_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/path-sum-ii/
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# Maintain a partial path and either make a new copy with latest node (as in path_sum) or append latest node
# and pop before returning (as in path_sum2, which is faster).
# Time - O(n)
# Space - O(n**2), every path of tree has correct sum

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
        self.path_sum(root, sum, [], paths)
        return paths

    def path_sum(self, node, target, partial, paths):

        if not node:
            return

        target -= node.val
        if target == 0 and not node.left and not node.right:
            paths.append(partial + [node.val])

        self.path_sum(node.left, target, partial + [node.val], paths)
        self.path_sum(node.right, target, partial + [node.val], paths)

    def path_sum2(self, node, target, partial, paths):

        if not node:
            return

        target -= node.val
        partial.append(node.val)
        if target == 0 and not node.left and not node.right:
            paths.append(partial[:])

        self.path_sum2(node.left, target, partial, paths)
        self.path_sum2(node.right, target, partial, paths)

        partial.pop()