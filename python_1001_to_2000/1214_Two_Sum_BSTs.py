_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/two-sum-bsts/
# Given two binary search trees, return True if and only if there is a node in the first tree and a node in
# the second tree whose values sum up to a given integer target.

# Explore the first tree by depth-first search, adding all values to a set.
# Explore the second tree by depth-first search, checking for each node if its complement to sum to target is in the
# set of values from the first tree.
# Note that this works for a binary tree even if it is not a search tree.
# Time - O(m + n) for trees of size m and n.
# Space - O(m + n)

class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        seen = set()

        def explore(node):
            if not node:
                return
            seen.add(node.val)
            explore(node.left)
            explore(node.right)

        explore(root1)

        def find(node):
            if not node:
                return False
            if target - node.val in seen:
                return True
            return find(node.left) or find(node.right)

        return find(root2)
