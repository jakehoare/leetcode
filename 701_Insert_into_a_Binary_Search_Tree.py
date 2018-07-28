_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into
# the BST. Return the root node of the BST after the insertion.
# It is guaranteed that the new value does not exist in the original BST.
# Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion.
# You can return any of them.

# Iterative solution. Move left or right according to whether val is less than or greater than current node.val, until
# an empty node is found.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        new_node = TreeNode(val)
        if not root:
            return new_node

        node = root

        while True:

            if val < node.val:
                if not node.left:
                    node.left = new_node
                    return root
                node = node.left

            else:
                if not node.right:
                    node.right = new_node
                    return root
                node = node.right