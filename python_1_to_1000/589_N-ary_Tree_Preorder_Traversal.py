_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/n-ary-tree-preorder-traversal/
# Given an n-ary tree, return the preorder traversal of its nodes' values.

# Stack contains nodes discovered and to be visited. Pop a node off the stack and append its value to the result.
# Add child nodes to stack in reverse order, so they are popped off in the original order.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []

        stack = [root]
        result = []

        while stack:

            node = stack.pop()
            result.append(node.val)

            for child in reversed(node.children):
                stack.append(child)

        return result