_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-tree-tilt/
# Given a binary tree, return the tilt of the whole tree.
# The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and
# the sum of all right subtree node values. Null node has tilt 0.
# The tilt of the whole tree is defined as the sum of all nodes' tilt.

# Recursive helper function returns the sum of the values in a tree. Tilt is the absolute difference between the
# left and right subtree sums.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tilt = 0       # instance variable collects sum

        def helper(node):

            if not node:    # base case
                return 0

            left, right = helper(node.left), helper(node.right)
            self.tilt += abs(left - right)  # update total tilt
            return node.val + left + right  # return sum of all values in tree

        helper(root)
        return self.tilt