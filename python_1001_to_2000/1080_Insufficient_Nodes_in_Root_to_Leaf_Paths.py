_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/
# Given the root of a binary tree, consider all root to leaf paths: paths from the root to any leaf.
# A leaf is a node with no children.
# A node is insufficient if every such root to leaf path intersecting this node has sum strictly less than limit.
# Delete all insufficient nodes simultaneously, and return the root of the resulting binary tree.

# Move down the tree, subtracting each node's value form the limit.
# If a leaf node has a value less than the limit then it is insufficient so remove it.
# Recurse to left and right subtrees if they exist.
# If either subtree is not removed then there is a path through a node greater than or equal to the limit,
# so retain the node, else remove it.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        if root.left is None and root.right is None:
            return None if root.val < limit else root

        if root.left:
            root.left = self.sufficientSubset(root.left, limit - root.val)
        if root.right:
            root.right = self.sufficientSubset(root.right, limit - root.val)

        return root if root.right or root.left else None
