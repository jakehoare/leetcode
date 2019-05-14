_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/robot-bounded-in-circle/
# On an infinite plane, a robot initially stands at (0, 0) and faces north.
# The robot can receive one of three instructions:
# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degress to the right.
# The robot performs the instructions given in order, and repeats them forever.
# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

# Track the robot's position and direction, updating after every move.
# If the direction is changed after all moves then the position will return to the origin after 2 or 4 repeats of the
# instructions. If the direction is unchanged then the position must also be unchanged.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        r, c = 0, 0
        dr, dc = 1, 0

        for instruction in instructions:
            if instruction == "G":
                r += dr
                c += dc
            elif instruction == "L":
                dr, dc = -dc, dr
            else:
                dr, dc = dc, -dr

        return (dr, dc) != (1, 0) or (r, c) == (0, 0)
