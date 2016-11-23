_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-search-tree-iterator/
# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
# Calling next() will return the next smallest number in the BST.
# next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

# Iterative inorder traversal.  Go left to smallest node, pushing all nodes onto stack.  After popping a node,
# add to stack all nodes on path to its inorder successor by moving to right child then as far left as possible.
# Time - O(n) worst case and O(1) average for __init__() and next().
# Space - O(n) worst case, log n if balanced.

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.stack else False

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        result = node.val
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        return result