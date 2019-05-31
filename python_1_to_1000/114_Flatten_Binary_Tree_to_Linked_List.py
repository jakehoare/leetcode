_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Given a binary tree, flatten it to a linked list in-place.
# Each node only has a right child.  Left subtree is flattened before right.

# Preorder traversal.  Records previous node visited as instance field.  Flattens left subtree then moves to right,
# deleting old left reference, before appending flattened right.
# Alternatively can find last node of flattened left by traversing.
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
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        self.prev = root        # update previous node to this node

        self.flatten(root.left)

        temp = root.right       # store right subtree and move previous left to right
        root.right = root.left
        root.left = None        # delete link to previous left

        self.prev.right = temp  # link last of flattened left to root of right subtree
        self.flatten(temp)
