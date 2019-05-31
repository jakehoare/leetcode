_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-binary-tree-ii/
# We are given the root node of a maximum tree: a tree where every node has a value greater than any other value in
# its subtree.
# The given tree was constructed from an list A (root = Construct(A)) recursively with the following Construct(A) fn:
# If A is empty, return null.
# Otherwise, let A[i] be the largest element of A.  Create a root node with value A[i].
# The left child of root will be Construct([A[0], A[1], ..., A[i-1]])
# The right child of root will be Construct([A[i+1], A[i+2], ..., A[A.length - 1]])
# Return root.
# Note that we were not given A directly, only a root node root = Construct(A).
# Suppose B is a copy of A with the value val appended to it.  It is guaranteed that B has unique values.
# Return Construct(B).

# The new value will always be a right child, since it is the last element of the input list.
# Move along the path of right children until there are no more right children or the node val is less than the new val.
# Add the new node as a right child. The old right subtree is the new left subtree of the new node, since all its
# elements are to the left of the new node in the list.
# Create a dummy root with infinite value to ensure the new node is always a child of some node.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        new_root = TreeNode(float("inf"))   # new root to handle special case of val > root.val
        new_root.right = root
        node = new_root

        while node.right and node.right.val > val:
            node = node.right

        right_subtree = node.right
        node.right = TreeNode(val)
        node.right.left = right_subtree

        return new_root.right
