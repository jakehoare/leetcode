_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/count-complete-tree-nodes/
# Given a complete binary tree, count the number of nodes.
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last
# level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Find depth of left most path in left and right subtrees.  If equal then left subtree is complete, if different
# then right subtree is complete.
# Alternatively, find depth of left path and right path, if equal return 2**depth -1.  If not recurse on subtrees,
# retaining know left path depth of left subtree and right path depth of right subtree.
# Time - O((log n)**2), height is log n since complete.  Recurse either left or right at each layer.
# Space - O(1)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left_subtree = self.left_depth(root.left)
        right_subtree = self.left_depth(root.right)

        if left_subtree == right_subtree:
            return 2**left_subtree + self.countNodes(root.right)    # 1 (root) + 2**left_subtree - 1 (left subtree)
        else:
            return 2**right_subtree + self.countNodes(root.left)


    def left_depth(self, node):
        depth = 0
        while node:
            node = node.left
            depth += 1
        return depth