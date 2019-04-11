_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# Given a binary tree, each node has value 0 or 1.
# Each root-to-leaf path represents a binary number starting with the most significant bit.
# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
# Return the sum of these numbers.

# For each node, update the previous value by multiplying by 2 (left bit shift) and adding the new bit.
# If the node is a leaf, return the updated value. Else recurse and sum the leaves in the left and right subtrees.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, running):

            if not node:
                return 0

            running = running * 2 + node.val
            if not node.left and not node.right:
                return running

            return helper(node.left, running) + helper(node.right, running)

        return helper(root, 0) % (10 ** 9 + 7)
