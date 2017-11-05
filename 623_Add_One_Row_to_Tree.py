_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/add-one-row-to-tree/
# Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given
# depth d. The root node is at depth 1.
# The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree
# nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left
# subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree
# root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root
# of the whole original tree, and the original tree is the new root's left subtree.

# If d == 1 create a new root. If d == 2 insert new nodes between root and its children. Else recurse to next depth.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if d == 1:              # create a new root and put existing tree on left
            root, root.left = TreeNode(v), root
        elif d == 2:            # new nodes as children of root
            old_left, old_right = root.left, root.right
            root.left, root.right = TreeNode(v), TreeNode(v)
            root.left.left, root.right.right = old_left, old_right
        else:                   # recurse at next depth
            self.addOneRow(root.left, v, d - 1)
            self.addOneRow(root.right, v, d - 1)

        return root