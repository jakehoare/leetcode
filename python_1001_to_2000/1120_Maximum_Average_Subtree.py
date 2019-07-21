_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-average-subtree/
# Share
# Given the root of a binary tree, find the maximum average value of any subtree of that tree.
# A subtree of a tree is any node of that tree plus all its descendants.
# The average value of a tree is the sum of its values, divided by the number of nodes.

# Helper function returns the count of nodes and their sum for subtree.
# Recurse left and right, updating the result from the subtree results.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        self.result = 0

        def helper(node):
            if not node:
                return 0, 0
            left_nodes, left_sum = helper(node.left)
            right_nodes, right_sum = helper(node.right)
            total_nodes = 1 + left_nodes + right_nodes
            total_sum = node.val + left_sum + right_sum
            self.result = max(self.result, total_sum / float(total_nodes))
            return total_nodes, total_sum

        helper(root)
        return self.result
