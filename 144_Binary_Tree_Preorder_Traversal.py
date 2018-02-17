_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Given a binary tree, return the preorder traversal of its nodes' values.

# Maintain a stack of nodes discovered and to be visited. Add right children to stack before left so left subtrees
# are visited before right.
# Alternatively, visit node, recurse left then recurse right.
# Time - O(n)
# Space - O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        preorder = []
        stack = [root]

        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)    # push right first so left is popped first
            if node.left:
                stack.append(node.left)

        return preorder


class Solution2(object):
    def preorderTraversal(self, root):
        result = []
        self.preorder(root, result)
        return result

    def preorder(self, node, result):
        if not node:
            return
        result.append(node.val)
        self.preorder(node.left, result)
        self.preorder(node.right, result)
