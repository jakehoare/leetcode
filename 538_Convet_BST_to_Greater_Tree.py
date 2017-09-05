_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/convert-bst-to-greater-tree/
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

# Reverse inorder traversal. Track running sum of all nodes visited with class instance variable.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def __init__(self):
        self.running_sum = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def rev_inorder(node):

            if not node:
                return

            rev_inorder(node.right)         # greater values on right
            node.val += self.running_sum
            self.running_sum = node.val     # sum of all previous nodes and this node
            rev_inorder(node.left)


        self.running_sum = 0    # reset if convertBST called again from same class instance
        rev_inorder(root)
        return root