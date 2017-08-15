_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/the-maze-iii/
# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up (u),
# down (d), left (l) or right (r), but it won't stop rolling until hitting a wall. When the ball stops, it could choose
# the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.
# Given the ball position, the hole position and the maze, find out how the ball could drop into the hole by moving
# the shortest distance. The distance is defined by the number of empty spaces traveled by the ball from the start
# position (excluded) to the hole (included). Output the moving directions by using 'u', 'd', 'l' and 'r'. Since there
# could be several different shortest ways, you should output the lexicographically smallest way.
# If the ball cannot reach the hole, output "impossible".

# Deque stores positions and previous direction. If can move in same direction, add to back of deque. If cannot, try
# to move in perpendicular directions by adding to front of deque.
# Time - O(mn)
# Space - O(mn)

from collections import deque

class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """

        def maze_cell(r, c):
            if [r, c] == hole:
                return -1
            elif 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] == 0:
                return 0
            return 1

        def vertical(dirn):
            return dirn in {"d", "u"}

        def perpendicular(dirn):
            return ["r", "l"] if vertical(dirn) else ["u", "d"]     # reverse lexicographical order

        visited = set()  # stores tuples (r, c, dirn)
        queue = deque()
        dirns = {"d": (1, 0), "u": (-1, 0), "r": (0, 1), "l": (0, -1)}
        for dirn in "dlru":
            queue.append((ball[0], ball[1], [dirn]))

        while queue:
            r, c, moves = queue.popleft()
            if (r, c, moves[-1]) in visited:
                continue
            visited.add((r, c, moves[-1]))

            dr, dc = dirns[moves[-1]]
            nm = maze_cell(r + dr, c + dc)

            if nm == -1:
                return "".join(moves)

            # move in same direction as previous if possible
            elif nm == 0:
                queue.append((r + dr, c + dc, moves))   # add to back of queue

            # else move in a perpendicular direction if possible and not at start
            elif [r, c] != ball:
                trial_dirns = perpendicular(moves[-1])
                for trial_dirn in trial_dirns:
                    queue.appendleft((r, c, moves + [trial_dirn]))  # add to front of queue

        return "impossible"

