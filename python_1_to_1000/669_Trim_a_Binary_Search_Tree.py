_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/trim-a-binary-search-tree/
# Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements
# lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of
# the trimmed binary search tree.

# If root val is in [L, R] then return root and trimmed left and right subtrees. If root is ledd than left, root and
# all smaller values in left subtree should be trimmed, so return trimmed right subtree.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.val > R:
            return self.trimBST(root.left, L, R)
        if root.val < L:
            return self.trimBST(root.right, L, R)

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root
