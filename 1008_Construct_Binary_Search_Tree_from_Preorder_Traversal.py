_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# Return the root node of a binary search tree that matches the given preorder traversal.
# Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a
# value < node.val, and any descendant of node.right has a value > node.val.
# Also recall that a preorder traversal displays the value of the node first, then traverses node.left,
# then traverses node.right.

# Helper function builds tree, provided the next value is below max_value.
# Create the subtree root and increment the next index of preorder. Then build the left subtree from elements < root,
# then build the right subtree from elements < max_value (value of parent of root).
# Time - O(n)
# Space - O(n)

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        self.i = 0          # index of next element to be added to tree

        def helper(max_value=float("inf")):
            if self.i >= len(preorder) or preorder[self.i] > max_value:
                return None

            root = TreeNode(preorder[self.i])
            self.i += 1
            root.left = helper(root.val)        # left subtree uses elements < root.val
            root.right = helper(max_value)      # right subtree uses elements < max_value
            return root

        return helper()
