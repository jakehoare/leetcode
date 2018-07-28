_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Given a binary tree, return the postorder traversal of its nodes' values.

# Maintain a stack of nodes discovered and to be visited. Nodes are added to front of result (or the end of a list
# which is reversed before returning result).
# Add left children to stack before right so right subtrees are visited before left.
# Alternatively, recurse left, recurse right then visit node.
# Time - O(n)
# Space - O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        result = deque()        # deque instead of list so we can append at front
        stack = [root]

        while stack:
            node = stack.pop()
            result.appendleft(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return list(result)


class Solution2(object):
    def postorderTraversal(self, root):
        result = []
        self.postorder(root, result)
        return result

    def postorder(self, node, result):
        if not node:
            return
        self.postorder(node.left, result)
        self.postorder(node.right, result)
        result.append(node.val)

