_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/walking-robot-simulation/
# A robot on an infinite grid starts at point (0, 0) and faces north.
# The robot can receive one of three possible types of commands:
# -2: turn left 90 degrees
# -1: turn right 90 degrees
# 1 <= x <= 9: move forward x units
# Some of the grid squares are obstacles.
# The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])
# If the robot would try to move onto them, the robot stays on the previous grid square instead (but still
# continues following the rest of the route.)
# Return the square of the maximum Euclidean distance that the robot will be from the origin.

# Track the postition and orientation of the robot. When moving forwards, check if the next position is an obstacle
# and stop if so.
# Time - O(n) total number of operations (since at most 9 steps forwards)
# Space - O(m) number of obstacles

class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]     # change of position in each direction

        position, orientation = (0, 0), NORTH
        max_sqr_distance = 0
        obstacles = {tuple(obstacle) for obstacle in obstacles}  # convert to set for O(1) lookup

        for command in commands:
            if command == -2:
                orientation = (orientation - 1) % 4         # turn left
            elif command == -1:
                orientation = (orientation + 1) % 4         # turn right
            else:
                for _ in range(command):
                    next_position = (position[0] + directions[orientation][0],
                                     position[1] + directions[orientation][1])
                    if next_position in obstacles:          # stop moving if obstacle
                        break
                    position = next_position
                    max_sqr_distance = max(max_sqr_distance, position[0] ** 2 + position[1] ** 2)

        return max_sqr_distance

