_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/path-sum/
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up
# all the values along the path equals the given sum.

# Base cases of False if no node and True if leaf node with correct sum.  Else subtract node value and check if
# True in either subtree.
# Time - O(n)
# Space - O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        sum -= root.val
        if sum == 0 and not root.left and not root.right:   # leaf node
            return True

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
