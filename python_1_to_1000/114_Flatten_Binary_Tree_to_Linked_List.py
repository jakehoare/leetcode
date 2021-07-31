_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Given a binary tree, flatten it to a linked list in-place.
# Each node only has a right child.  Left subtree is flattened before right.

# Records the root of the previous subtree flattened as an instance field.
# Flattens right subtree, after which self.prev is the root of the right subtree.
# Then connects the flattened left subtree to the flattened right subtree.
# Then removes the link from the root to the old left subtree, and sets the
# root.right to the root of the left subtree (now flattened).
# Time - O(n)
# Space - O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):         # instance field self.prev to track previous node
        self.prev = None

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        self.flatten(root.right)
        self.flatten(root.left)
        
        root.left = None
        root.right = self.prev
        self.prev = root        
