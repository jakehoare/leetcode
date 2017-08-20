_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-bottom-left-tree-value/
# Given a binary tree, find the leftmost value in the last row of the tree.

# BFS from right to left so final node is left most.
# Time - O(n)
# Space - O(n)

from collections import deque

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return node.val