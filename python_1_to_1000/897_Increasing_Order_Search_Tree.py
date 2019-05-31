_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/increasing-order-search-tree/
# Given a tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree,
# and every node has no left child and only 1 right child.

# Amend the function signature so it converts a tree and then appends a tail tree.
# Create a new node with same value as the root, so references to the root's children are retained. Convert the right
# subtree and append the tail. Convert the left subtree and append the right subtree.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def increasingBST(self, root, tail=None):       # tail is appended after converting tree from root
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return tail

        copy_root = TreeNode(root.val)              # make a duplicate, so root.left and root.right are retained
        copy_root.right = self.increasingBST(root.right, tail)
        return self.increasingBST(root.left, copy_root)