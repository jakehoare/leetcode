_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/leaf-similar-trees/
# Consider all the leaves of a binary tree.
# From left to right order, the values of those leaves form a leaf value sequence.
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

# Generate the leaves by inorder traversal. Yield from the left subtree, yield the node value then yield from the
# right subtree. Zip the inorder traversals together up to the longest sequence and check all values are equal.
# Time - O(n)
# Space - O(1)

import itertools

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def inorder(node):
            if node.left:                           # check left subtree
                yield from inorder(node.left)
            if not node.left and not node.right:    # yield the leaf val
                yield node.val
            if node.right:                          # check right subtree
                yield from inorder(node.right)

        leaves = itertools.zip_longest(inorder(root1), inorder(root2))

        return all(l1 == l2 for l1, l2 in leaves)