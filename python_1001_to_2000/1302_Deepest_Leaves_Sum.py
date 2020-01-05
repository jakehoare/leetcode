_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/deepest-leaves-sum/
# Given a binary tree, return the sum of values of its deepest leaves.

# Breadth-first search.
# For each layer, sum all the node values and find all nodes in the next layer.
# Repeat until the layer is empty and return the sum of nodes in the previous layer.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = [root]

        while nodes:
            level_sum = 0
            new_nodes = []

            for node in nodes:
                level_sum += node.val
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)

            nodes = new_nodes

        return level_sum
