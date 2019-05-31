_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/invert-binary-tree/
# Invert a binary tree.

# Left substree is old right subtree inverted. Right subtree is old left subtree inverted.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root
