_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/brick-wall/
# There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the
# same height but different width. You want to draw a vertical line from the top to the bottom and cross the least
# bricks.
# The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each
# brick in this row from left to right.
# If your line go through the edge of a brick, then the brick is not considered as crossed.
# You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.
# You cannot draw a line just along one of the two vertical edges of the wall.

# Count number of bricks in wall with right edges at every position. Choose the position with the most edges.
# Time - O(n), number of bricks
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        edges = defaultdict(int)  # mapping from x-position of an edge to count of number of edges

        for row in wall:
            edge = 0

            for brick in row:
                edge += brick
                edges[edge] += 1

        del edges[sum(wall[0])]  # delete RHS vertical edge

        crossed = len(wall)  # cross all brick if no edges, else choose path with most edges
        return crossed if not edges else crossed - max(edges.values())