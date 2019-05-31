_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/
# Given a binary tree with N nodes, each node has a different value from {1, ..., N}.
# A node in this binary tree can be flipped by swapping the left child and the right child of that node.
# Consider the sequence of N values reported by a preorder traversal starting from the root.
# Call such a sequence of N values the voyage of the tree.
# Recall that a preorder traversal of a node means we report the current node's value, then preorder-traverse the
# left child, then preorder-traverse the right child.
# Our goal is to flip the least number of nodes so that the voyage of the tree matches the voyage we are given.
# If we can do so, then return a list of the values of all nodes flipped. You may return the answer in any order.
# If we cannot do so, then return the list [-1].

# Recursive helper function returns whether subtree can be flipped to match voyage and increments index of next
# element of voyage to be tested. Note that voyage is the same length as the number of nodes in the tree.
# After checking the root against voyage, if there is a left child that doesn't match the next element of voyage
# then there must be a flip. If no left child, the next element of voyage must match the right child (if any).
# Time - O(n)
# Space - O(n)

class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        flipped = []
        self.i = 0              # index of next node in voyage

        def preorder(node):     # returns False if voyage cannot be matched by traversal
            if not node:
                return True

            if voyage[self.i] != node.val:  # must match root
                return False
            self.i += 1

            if node.left:

                if node.left.val != voyage[self.i]:
                    flipped.append(node.val)
                    node.left, node.right = node.right, node.left
                if not preorder(node.left): # recurse with left subtree
                    return False

            return preorder(node.right)

        return flipped if preorder(root) else [-1]