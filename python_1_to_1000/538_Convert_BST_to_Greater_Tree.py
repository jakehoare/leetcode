_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/convert-bst-to-greater-tree/
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to
# the original key plus sum of all keys greater than the original key in BST.

# Reverse inorder traversal. Visit right subtree (containing all greater values), update node value and running sum,
# then visit left subtree.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.running_sum = 0

        def inorder(node):
            if not node:
                return

            inorder(node.right)

            node.val += self.running_sum
            self.running_sum = node.val

            inorder(node.left)

        inorder(root)
        return root