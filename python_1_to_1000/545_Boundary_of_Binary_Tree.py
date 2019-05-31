_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/boundary-of-binary-tree/
# Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary
# includes left boundary, leaves, and right boundary in order without duplicate nodes.
# Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from
# root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left
# boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.
# The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree
# if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.
# The right-most node is also defined by the same way with left and right exchanged.

# Find left edge until leaf. Inorder traversal to append all leaves. Find right edge and reverse.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def left_side(node):
            if not node or (not node.left and not node.right):
                return
            boundary.append(node.val)
            if node.left:
                left_side(node.left)
            else:
                left_side(node.right)

        def right_side(node):
            if not node or (not node.left and not node.right):
                return
            right_edge.append(node.val)
            if node.right:
                right_side(node.right)
            else:
                right_side(node.left)

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if not node.left and not node.right:
                boundary.append(node.val)
            inorder(node.right)

        if not root:
            return []

        boundary, right_edge = [root.val], []

        # ignore root
        left_side(root.left)
        inorder(root.left)
        inorder(root.right)
        right_side(root.right)

        return boundary + right_edge[::-1]