_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
# Given a binary tree, determine if it is a complete binary tree.
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the
# last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Maintain a queue of nodes discovered. Explore the tree layer by layer (breadth-first search).
# When the first empty node is found, check if all other nodes are empty. Else add children to the queue.
# Time - O(n)
# Space - O(n)

from collections import deque

class Solution:
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = deque([root])

        while True:

            node = queue.popleft()
            if not node:
                return all(not nd for nd in queue)

            queue.append(node.left)
            queue.append(node.right)