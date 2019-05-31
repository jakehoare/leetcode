_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/
# Given a binary tree, find the length of the longest consecutive sequence path.  The path refers to any sequence
# of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive
# path must be from parent to child (cannot be the reverse).

# Preorder traversal.  If a node is 1 + previous value then increment sequence length, else start a new sequence.
# Time - O(n)
# Space - O(1)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0
        self.consecutive(root, float('inf'), 0)
        return self.longest

    def consecutive(self, node, parent_val, sequence):
        if not node:
            return

        if node.val == 1 + parent_val:
            sequence += 1
        else:
            sequence = 1
        self.longest = max(self.longest, sequence)

        self.consecutive(node.left, node.val, sequence)
        self.consecutive(node.right, node.val, sequence)
