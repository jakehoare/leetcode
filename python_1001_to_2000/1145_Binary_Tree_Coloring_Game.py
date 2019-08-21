_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-tree-coloring-game/
# Two players play a turn based game on a binary tree.
# We are given the root of this binary tree, and the number of nodes n in the tree.
# n is odd, and each node has a distinct value from 1 to n.
# Initially, the first player names a value x with 1 <= x <= n,
# and the second player names a value y with 1 <= y <= n and y != x.
# The first player colors the node with value x red, and the second player colors the node with value y blue.
# Then, the players take turns starting with the first player.
# In each turn, that player chooses any node of their color (red if player 1, blue if player 2)
# and colors an uncolored neighbor of the chosen node (either the left child, right child, or parent of the node.)
# If (and only if) a player cannot choose such a node in this way, they must pass their turn.
# If both players pass their turn, the game ends, and the winner is the player that colored more nodes.
# You are the second player.
# If it is possible to choose such a y to ensure you win the game, return true.
# If it is not possible, return false.

# Count the nodes from the root excluding those after the red node.
# Also count the left and right subtrees of the red node.
# The second player should colour the parent, left child or right child of the red node.
# If the most nodes controlled from any of those locations is greater than the nodes in the other locations + the
# initial red node, then the second player can win.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        self.left, self.right = 0, 0

        def count(node):
            if not node:
                return 0

            if node.val == x:       # count child subtrees
                self.left = count(node.left)
                self.right = count(node.right)
                return 0

            return 1 + count(node.left) + count(node.right)

        parent = count(root)
        results = sorted([parent, self.left, self.right])

        return results[-1] > sum(results[:2]) + 1
