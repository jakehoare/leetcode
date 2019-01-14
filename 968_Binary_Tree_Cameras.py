_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-tree-cameras/
# Given a binary tree, we install cameras on the nodes of the tree.
# Each camera at a node can monitor its parent, itself, and its immediate children.
# Calculate the minimum number of cameras needed to monitor all nodes of the tree.

# Bottom-up recursion. Helper function returns the number of cameras to cover a subtree, apart from potentially not
# covering the root. Maintain a set of nodes that are covered.
# After processing child subtrees, if either child is not covered then there must be a camera at the node and hence
# its parent is also covered.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        covered = {None}                # empty leaves are always covered

        def helper(node, parent):       # returns number of cameras to cover subtree apart from node

            if not node:
                return 0

            result = helper(node.left, node) + helper(node.right, node)     # recurse for children first (bottom-up)

            if node.left not in covered or node.right not in covered:       # must put a camera at node
                covered.update({parent, node, node.left, node.right})       # node and neighbours are now covered
                result += 1

            return result

        cameras = helper(root, None)
        return cameras if root in covered else cameras + 1                  # potentially add camera at root
