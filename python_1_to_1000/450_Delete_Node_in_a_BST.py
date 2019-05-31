_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/delete-node-in-a-bst/
# Given a root node reference of a BST and a key, delete the node with the given key in the BST.
# Return the root node reference (possibly updated) of the BST.

# Recursively test if key is root value. If not recurse left or right and update subtree. If root has key, replace root
# value with next largest value and recurse to update root right subtree having deleted node with next largest value.
# Time - O(n), height of tree
# Space - O(1)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if key > root.val:  # key in right subtree, keep root and update right subtree
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:
            if not (root.left and root.right):  # one or no children
                root = root.left or root.right
            else:  # both children
                next_largest = root.right
                while next_largest.left:
                    next_largest = next_largest.left
                root.val = next_largest.val
                root.right = self.deleteNode(root.right, root.val)

        return root