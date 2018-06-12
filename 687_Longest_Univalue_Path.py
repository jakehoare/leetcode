_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-univalue-path/
# Given a binary tree, find the length of the longest path where each node in the path has the same value.
# This path may or may not pass through the root.
# The length of path between two nodes is represented by the number of edges between them.

# Helper function updates longest for the univalue path that goes through each node. Helper returns a tuple of the
# longest paths via the left and right children of each node.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0

        def helper(node):
            if not node:
                return 0, 0

            max_left = max(helper(node.left))       # longest univalue path from left child
            max_right = max(helper(node.right))

            # if left child has the same val as node, add one edge to longest path via left child
            left = 1 + max_left if node.left and node.left.val == node.val else 0
            right = 1 + max_right if node.right and node.right.val == node.val else 0

            self.longest = max(self.longest, left + right)

            return left, right

        helper(root)
        return self.longest