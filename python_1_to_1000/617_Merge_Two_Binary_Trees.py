_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/merge-two-binary-trees/
# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees
# are overlapped while the others are not.
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values
# up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

# If either or both of t1 and t2 are None, return t1 or t2. Else create a root node with the sum of the values and
# recursively create the left and right subtrees.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)

            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)

            return root

        return t1 or t2