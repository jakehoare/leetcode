_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/squirrel-simulation/
# There's a tree, a squirrel, and several nuts. Positions are represented by the cells in a 2D grid. Your goal is to
# find the minimal distance for the squirrel to collect all the nuts and put them under the tree one by one. The
# squirrel can only take at most one nut at one time and can move in four directions - up, down, left and right, to
# the adjacent cell. The distance is represented by the number of moves.

# The only choice to make is which nut to collect first. The distance for all other nuts is from the tree to the nut
# and back. For each starting nut, calculate the change in distance by going from squirrel to nut and not from
# tree to nut. Add the greatest reduction in distance to the round-trips for all nuts.
# Time - O(n) number of nuts
# Space - O(1)

class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        if not nuts:
            return 0

        nuts_to_tree = 0  # sum of all distances from nut to tree
        best_gain = height * width  # best change in total distance

        def distance(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        for nut in nuts:
            nut_to_tree = distance(nut, tree)
            squirrel_to_nut = distance(squirrel, nut)
            nuts_to_tree += nut_to_tree
            best_gain = min(best_gain, squirrel_to_nut - nut_to_tree)

        return 2 * nuts_to_tree + best_gain

