_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/construct-quad-tree/
# We want to use quad trees to store an N x N boolean grid. Each cell in the grid can only be true or false.
# The root node represents the whole grid. For each node, it will be subdivided into four children nodes until the
# values in the region it represents are all the same.
# Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node.
# The val attribute for a leaf node contains the value of the region it represents.
# Your task is to use a quad tree to represent a given grid.
# For the non-leaf nodes, val is True if any of the child node vals are True.
# N is less than 1000 and guaranteed to be a power of 2.

# Bottom-up recursion. Base case of a single cell. For any grid, recurse for each of the 4 quadrants. If all are
# leaves with the same value, the root representing the grid is also a leaf. Else the root is a node with children of
# the 4 quadrant nodes.
# Time - O(n**2)
# Space - O(n**2)

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def helper(r, c, side):     # construct quad tree for grid from cell (r, c) with side length of side

            if side == 1:           # base case of single cell
                return Node(bool(grid[r][c]), True, None, None, None, None)

            top_left = helper(r, c, side // 2)
            top_right = helper(r, c + side // 2, side // 2)
            bottom_left = helper(r + side // 2, c, side // 2)
            bottom_right = helper(r + side // 2, c + side // 2, side // 2)

            if top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf:
                if top_left.val == top_right.val == bottom_left.val == bottom_right.val:
                    return Node(top_left.val, True, None, None, None, None)

            node_val = any((top_left.val, top_right.val, bottom_left.val, bottom_right.val))
            return Node(node_val, False, top_left, top_right, bottom_left, bottom_right)

        if not grid:
            return None
        return helper(0, 0, len(grid))