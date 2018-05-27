_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/construct-string-from-binary-tree/
# You need to construct a string consists of parenthesis and integers from a binary tree in a preorder traversal.
# The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis
# pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

# Preorder traversal. Append to the result the string of the node.val. If neither left nor right children, return.
# Add brackets before and after left subtree, since empty brackets are required if left subtree is None. If right
# subtree exists, add brackets before and after it.
# Time - O(n)
# Space - O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        result = []

        def preorder(node):

            if not node:
                return

            result.append(str(node.val))

            if not node.left and not node.right:
                return

            result.append("(")
            preorder(node.left)
            result.append(")")

            if node.right:
                result.append("(")
                preorder(node.right)
                result.append(")")

        preorder(t)
        return "".join(result)