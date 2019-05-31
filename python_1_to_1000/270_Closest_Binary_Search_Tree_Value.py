_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/closest-binary-search-tree-value/
# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.

# If target is node val then return. Update closest if node val is closer. If target is more than root val then
# no value in left subtree can be closer than node.val so move to right subtree. Vica versa for left subtree.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closest = root.val

        while root:

            if root.val == target:      # early return since cannot improve
                return root.val

            if abs(root.val - target) < abs(closest - target):
                closest = root.val

            if target < root.val:
                root = root.left
            else:
                root = root.right

        return closest
