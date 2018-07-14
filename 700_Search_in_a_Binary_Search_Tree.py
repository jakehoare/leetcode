_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/search-in-a-binary-search-tree/
# Given the root node of a binary search tree (BST) and a value.
# You need to find the node in the BST that the node's value equals the given value.
# Return the subtree rooted with that node. If such node doesn't exist, you should return None.

# At each node, return if node has target val else recurse right or left depending whether val is greater or less than
# node.val.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:                # val is not in tree
            return None

        if root.val == val:
            return root

        if val > root.val:
            return self.searchBST(root.right, val)
        return self.searchBST(root.left, val)