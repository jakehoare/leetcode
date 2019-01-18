_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/robot-room-cleaner/
# Given a robot cleaner in a room modeled as a grid.
# Each cell in the grid can be empty or blocked.
# The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.
# When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.
# Design an algorithm to clean the entire room using only the 4 given APIs shown below.
# boolean move() - returns True if it is possible to move in the current facing direction
# void turnLeft()
# void turnRight()
# void clean()

# Depth-first search. Each state is a location and direction. Clean the location and add to visited set.
# For each of the 4 neighbouring cells, if neighbour has not been visited and can be moved to, recurse to visit
# neighbour, then move back to original cell and turn left.
# Time - O(mn)
# Space - O(mn)

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()

        def dfs(x, y, dx, dy):

            robot.clean()
            visited.add((x, y))

            for _ in range(4):

                if ((x + dx, y + dy)) not in visited and robot.move():
                    dfs(x + dx, y + dy, dx, dy)
                    robot.turnLeft()        # revert to original position and direction
                    robot.turnLeft()
                    robot.move()
                    robot.turnLeft()
                    robot.turnLeft()

                robot.turnLeft()
                dx, dy = -dy, dx

        dfs(0, 0, 0, 1)
