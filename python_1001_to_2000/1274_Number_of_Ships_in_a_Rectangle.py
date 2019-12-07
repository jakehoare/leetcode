_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-ships-in-a-rectangle/
# This problem is an interactive problem.
# On the sea represented by a cartesian plane,
# each ship is located at an integer point, and each integer point may contain at most 1 ship.
# You have a function Sea.hasShips(topRight, bottomLeft) which takes two points as arguments
# and returns true if and only if there is at least one ship in the rectangle represented by the two points,
# including on the boundary.
# Given two points, which are the top right and bottom left corners of a rectangle,
# return the number of ships present in that rectangle.
# It is guaranteed that there are at most 10 ships in that rectangle.
# Submissions making more than 400 calls to hasShips will be judged Wrong Answer.
# Also, any solutions that attempt to circumvent the judge will result in disqualification.

# Split any rectangle with either non-zero side length containing a ship into 2 sections along the longest axis.
# Repeat until rectangle is empty or is a single point with a ship.
# Time - O(mn), may split to each point of initial rectangle.
# Space - O(mn)

class Solution(object):
    def countShips(self, sea, topRight, bottomLeft):
        """
        :type sea: Sea
        :type topRight: Point
        :type bottomLeft: Point
        :rtype: integer
        """
        def counter(top_right, bottom_left):
            if not sea.hasShips(top_right, bottom_left):
                return 0                            # no need to keep exploring
            x_dist = top_right.x - bottom_left.x
            y_dist = top_right.y - bottom_left.y
            if x_dist == 0 and y_dist == 0:         # rectangle is a point containing a ship
                return 1

            if x_dist > y_dist:                     # split along x
                x_mid = bottom_left.x + x_dist // 2
                return counter(Point(x_mid, top_right.y), bottom_left) + counter(top_right,
                                                                                 Point(x_mid + 1, bottom_left.y))
            else:                                   # split along y
                y_mid = bottom_left.y + y_dist // 2
                return counter(Point(top_right.x, y_mid), bottom_left) + counter(top_right,
                                                                                 Point(bottom_left.x, y_mid + 1))

        return counter(topRight, bottomLeft)

