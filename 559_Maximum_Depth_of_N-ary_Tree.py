_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
# Given a n-ary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Recursive function. Base cases of no node or leaf node. Else add 1 to the max depth of any child.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:   # required to avoid taking max of empty sequence
            return 1

        return 1 + max(self.maxDepth(child) for child in root.children)