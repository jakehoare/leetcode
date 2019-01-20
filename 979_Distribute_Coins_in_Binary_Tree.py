_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/distribute-coins-in-binary-tree/
# Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.
# In one move, we may choose two adjacent nodes and move one coin from one node to another.
# The move may be from parent to child, or from child to parent.
# Return the number of moves required to make every node have exactly one coin.

# Bottom-up recursion. Helper function takes a node and its parent and distributes coins evenly in the subtree rooted
# at the node, by pushing or pulling excess coins to or from the parent.
# Time - O(n)
# Space - O(n)

class Solution:
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, parent):

            if not node:
                return 0

            left = helper(node.left, node)          # distribute coins evenly in subtrees
            right = helper(node.right, node)

            upshift = node.val - 1                  # the number of coins to be pushed up to the parent (may be -ve)
            if upshift != 0:                        # no parent if node is root
                parent.val += upshift
            node.val = 1                            # node is now balanced
            return left + right + abs(upshift)      # total coins moved

        return helper(root, None)
