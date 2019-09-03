_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
# Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

# Traverse the tree with depth-first search, updating the sum of values at each level.
# Find the greatest sum of levels, then return the lowest level with that sum.
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level_sums = defaultdict(int)   # map level to sum of node values

        def helper(node, level):
            if not node:
                return

            level_sums[level] += node.val
            helper(node.left, level + 1)
            helper(node.right, level + 1)

        helper(root, 1)
        max_level_sum = max(level_sums.values())
        return min(level for level, level_sum in level_sums.items() if level_sum == max_level_sum)
