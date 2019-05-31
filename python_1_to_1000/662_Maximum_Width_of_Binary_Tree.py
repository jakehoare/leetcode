_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-width-of-binary-tree/
# Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum
# width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.
# The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in
# the level, where the null nodes between the end-nodes are also counted into the length calculation.

# For each level, create a list of all non-null nodes at the next level along with their indices. Indices are relative
# to a complete binary tree i.e. left most node has index 0 and right most 2**depth - 1. Width is separation between
# first and last nodes at each level.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        max_width = 1
        nodes = [(root, 0)]     # list of nodes per level and their indices

        while True:
            new_nodes = []

            for node, i in nodes:
                if node.left:
                    new_nodes.append((node.left, i * 2))
                if node.right:
                    new_nodes.append((node.right, i * 2 + 1))

            if not new_nodes:
                break
            nodes = new_nodes
            max_width = max(max_width, 1 + nodes[-1][1] - nodes[0][1])

        return max_width