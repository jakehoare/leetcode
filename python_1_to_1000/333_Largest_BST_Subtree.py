_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/largest-bst-subtree/
# Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree
# with largest number of nodes in it.

# Bottom-up recursively determine whether a subtree is a BST if its children and BSTs and he root node value is
# between the highest in left subtree and smallest in right subtree.
# Time - O(n)
# Space - O(1)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.largest = 0

        def is_bst(node):   # return largest in subtree, smallest in subtree, subtree count
                            # subtree count = -1 if not a BST
            if not node:
                return float("-inf"), float("inf"), 0

            left_bst = is_bst(node.left)
            right_bst = is_bst(node.right)

            if left_bst[2] != -1 and right_bst[2] != -1:        # both sides are BSTs
                if left_bst[0] < node.val < right_bst[1]:       # node.val within bounds set by subtrees
                    size = 1 + left_bst[2] + right_bst[2]       # update largest
                    self.largest = max(self.largest, size)
                    return max(right_bst[0], node.val), min(left_bst[1], node.val), size

            return 0, 0, -1

        is_bst(root)    # ignore return value
        return self.largest

