_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as
# the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

# If both p and q are more than the node value then the common ancestor must be on the right. Similarly on the left if
# p and q are lower. Else this is the common ancestor. Could also be iterative instead of recursive.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root