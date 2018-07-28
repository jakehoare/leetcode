_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/n-ary-tree-postorder-traversal/
# Given an n-ary tree, return the postorder traversal of its nodes' values.

# Visit the nodes in reverse postorder and reverse the result i.e. visit a node, then the children in reverse order.
# Stack contains nodes discovered and to be visited.
# While stack, pop off a node and visit it. Add children to stack in given order, so they are visited in reverse order.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def postorder(self, root):
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

            for child in node.children:
                stack.append(child)

        return result[::-1]