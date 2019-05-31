_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sum-of-left-leaves/
# Find the sum of all left leaves in a given binary tree.

# If node has a left child with no children then return the left child val + recurse right. Else recurse left and right.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)

        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)