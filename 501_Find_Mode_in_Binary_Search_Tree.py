_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-mode-in-binary-search-tree/
# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequent elements) in the BST.
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.

# Inorder traversal visiting each node in sorted order. If a node value is the same as the previous node value then
# extend the current sequence. Else start a new sequence. If a sequence has the same count as the previous mode then
# add the value to the mode list. If a sequence has a greater count than the previous mode then value is the only mode.
# Time - O(n)
# Space - O(n) if all values are unique.

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.prev = float("inf")
        self.count = 0
        self.mode_count = 0
        modes = []                  # mutable, not an instance variable

        def inorder(node):

            if not node:            # base case
                return

            inorder(node.left)      # recurse left

            if node.val == self.prev:   # extend sequence of same value
                self.count += 1
            else:
                self.prev = node.val    # start new sequence
                self.count = 1

            if self.count == self.mode_count:
                modes.append(node.val)  # another mode with same count as existing mode(s)
            elif self.count > self.mode_count:
                self.mode_count = self.count    # new unique mode
                modes.clear()                   # Python 3.3+, else pop until empty or use instance variable
                modes.append(node.val)

            inorder(node.right)

        inorder(root)
        return modes
