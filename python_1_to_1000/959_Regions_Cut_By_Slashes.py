_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/regions-cut-by-slashes/
# In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.
# These characters divide the square into contiguous regions.
# (Note that backslash characters are escaped, so a \ is represented as "\\".)
# Return the number of regions.

# Create graph where each cell of grid has 4 nodes, one for each edge.
# Connect edge nodes to neighbouring cells and make connections within a cell's edge nodes according to the slash.
# Connections are undirected, hence only one direction of a connection is required.
# Union-find each pair of nodes connected by an edge and count the number of ultimate parents.
# Time - O(n**2 log*n)
# Space - O(n**2)

class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n= len(grid)
        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

        parents = {}                                # map cell (r, c, dirn) to its parent

        def find(node):                             # return ultimate parent of a node
            parents.setdefault(node, node)
            while parents[node] != node:
                parents[node] = parents[parents[node]]  # collapse links
                node = parents[node]
            return node

        def union(node1, node2):                    # union ultimate parents
            parent1, parent2 = find(node1), find(node2)
            parents[parent2] = parent1

        for r in range(n):
            for c in range(n):
                if r != n - 1:                   # connect to cell below
                    union((r, c, DOWN), (r + 1, c, UP))
                if c != n - 1:                   # connect to cell to right
                    union((r, c, RIGHT), (r, c + 1, LEFT))

                if grid[r][c] == "/":               # connect pairs of edge nodes within cell if slash
                    union((r, c, UP), (r, c, LEFT))
                    union((r, c, DOWN), (r, c, RIGHT))
                elif grid[r][c] == "\\":
                    union((r, c, UP), (r, c, RIGHT))
                    union((r, c, DOWN), (r, c, LEFT))
                else:                               # connect all edge nodes
                    union((r, c, UP), (r, c, LEFT))
                    union((r, c, UP), (r, c, DOWN))
                    union((r, c, UP), (r, c, RIGHT))

        return len({find(node) for node in parents.keys()})     # number of ultimate parents
