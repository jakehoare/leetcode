_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/inorder-successor-in-bst-ii/
# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
# The successor of a node p is the node with the smallest key greater than p.val.
# You will have direct access to the node but not to the root of the tree.
# Each node will have a reference to its parent node.

# We want to perform the next visit in an inorder traversal from a given starting node. There are 2 cases:
# 1) If the starting node has a right child we move to the right child then repeatedly moves to the left child.
# When inorder(node.left) returns, there is no left child and we have found the successor.
# 2) Otherwise (no starting node right child) the next node visited is after returning to the parent.
# We move up the tree until we find a node that is the left child of its parent. The parent is then the successor.
# The first case is when the successor is further down the tree and within the subtree rooted at the starting node.
# In the second case we must move up the tree.
# Note that there may be no node that is a left child of its parent,
# in which case we have the last node of the inorder traversal (highest value) which has no successor.

# Time - O(n)
# Space - O(1)

class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node.right:
            node = node.right  # move right
            while node.left:
                node = node.left  # then as far left as possible
            return node

        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent
