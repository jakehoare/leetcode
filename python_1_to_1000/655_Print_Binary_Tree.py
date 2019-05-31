_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/print-binary-tree/
# Print a binary tree in an m*n 2D string array following these rules:
# The row number m should be equal to the height of the given binary tree.
# The column number n should always be an odd number.
# The root node's value (in string format) should be put in the exactly middle of the first row it can be put.
# The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part
# and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in
# the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one
# subtree is none while the other is not, you don't need to print anything for the none subtree but still need to
# leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need
# to leave space for both of them.
# Each unused space should contain an empty string "".
# Print the subtrees following the same rules.

# Find the height and calculate the width as 2**height - 1. Create an empty list of lists to hold result. The preorder
# traverse the tree, placing each value in the result and recursing to subtrees.
# Time - O(2 ** (n + 1)), every node visited once but worst case time is to create result when height = n
# Space - O(2 ** (n + 1))

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """

        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        rows = height(root)
        cols = 2 ** rows - 1

        result = [["" for _ in range(cols)] for _ in range(rows)]

        def place(node, r, c):
            if not node:
                return
            result[r][c] = str(node.val)
            shift = 2 ** (rows - r - 2)     # next column shift as a function of r
            place(node.left, r + 1, c - shift)
            place(node.right, r + 1, c + shift)

        place(root, 0, cols // 2)
        return result