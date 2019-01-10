_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/univalued-binary-tree/
# A binary tree is univalued if every node in the tree has the same value.
# Return true if and only if the given tree is univalued.

# Store root value. Check if each node has the same value and recurse for children.
# Time - O(n)
# Space - O(n)

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        value = root.val        # root is guaranteed not to be None

        def helper(node):
            if not node:
                return True
            if node.val != value:
                return False
            return helper(node.left) and helper(node.right)

        return helper(root)