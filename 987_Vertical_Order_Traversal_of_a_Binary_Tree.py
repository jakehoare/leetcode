_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# Given a binary tree, return the vertical order traversal of its nodes values.
# For each node at position (X, Y), its left and right children respectively will be at positions
# (X-1, Y-1) and (X+1, Y-1).
# Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes,
# we report the values of the nodes in order from top to bottom (decreasing Y coordinates).
# If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.
# Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

# Traverse the tree, creating a mapping from the x-coordinate of each node to a tuple of its y-coordinate and value.
# For each x-coordinate sorted in ascending order, sort the nodes by descending y-coordinate and value.
# Time - O(n log n), to sort the x-coord. Sorting the y-coords takes the same or less.
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        x_to_y_and_val = defaultdict(list)

        def helper(node, x, y):
            if not node:
                return
            x_to_y_and_val[x].append((-y, node.val))    # negative y-coordinate to later sort descending
            helper(node.left, x - 1, y - 1)
            helper(node.right, x + 1, y - 1)

        helper(root, 0, 0)
        result = []

        xs = sorted(x_to_y_and_val.keys())
        for x in xs:
            x_to_y_and_val[x].sort()
            result.append([val for _, val in x_to_y_and_val[x]])

        return result
