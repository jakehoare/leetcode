_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
# Given a rooted binary tree, return the lowest common ancestor of its deepest leaves.
# Recall that:
# The node of a binary tree is a leaf if and only if it has no children
# The depth of the root of the tree is 0, and if the depth of a node is d, the depth of each of its children is d+1.
# The lowest common ancestor of a set S of nodes is the node A with the largest depth,
# such that every node in S is in the subtree with root A.

# Helper function returns lca of deepest leaves and deepest leaf depth.
# Recurse to left and right subtrees.
# If depths are equal, current node is the lowest common ancestor.
# Else return the lca with the deepest depth and increment the depth.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def helper(node):
            if not node:
                return None, 0

            left_lca, left_depth = helper(node.left)
            right_lca, right_depth = helper(node.right)
            if left_depth == right_depth:
                return node, left_depth + 1

            if left_depth > right_depth:
                return left_lca, left_depth + 1
            return right_lca, right_depth + 1

        result, _ = helper(root)
        return result
