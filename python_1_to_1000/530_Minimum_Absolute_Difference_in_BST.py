_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
# Given a binary search tree with non-negative values, find the minimum absolute difference between values of
# any two nodes.

# Inorder traversal, visits nodes in order of ascending value. Track the value of the previous node visited. For each
# node update the min_diff with the difference between node.val and prev, if lower than current min_diff.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def getMinimumDifference(self, root):
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