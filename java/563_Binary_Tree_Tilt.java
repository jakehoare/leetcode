/*
https://leetcode.com/problems/binary-tree-tilt/
Given a binary tree, return the tilt of the whole tree.
The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the
sum of all right subtree node values. Null node has tilt 0.
The tilt of the whole tree is defined as the sum of all nodes' tilt.

Helper function returns sum of tree. Recursively call helper on subtrees. Update tilt then return tree sum.
Time - O(n)
Space - O(n), logn if balanced tree
*/

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tilt = 0       # instance variable

        def helper(node):

            if not node:
                return 0

            left_sum = helper(node.left)
            right_sum = helper(node.right)
            self.tilt += abs(left_sum - right_sum)
            return left_sum + right_sum + node.val

        helper(root)
        return self.tilt
