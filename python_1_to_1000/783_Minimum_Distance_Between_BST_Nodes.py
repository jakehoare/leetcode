_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
# Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any
# two different nodes in the tree.

# Inorder traversal visits nodes in increasing order of value. Update the previous node and minimum difference for
# each node.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.min_diff = float("inf")
        self.prev = float("-inf")

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val

            inorder(node.right)

        inorder(root)
        return self.min_diff