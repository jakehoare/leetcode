_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/the-maze-ii/
# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down,
# left or right, but it won't stop rolling until hitting a wall. When the ball stops, it can choose the next direction.
# Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the
# destination. The distance is defined by the number of empty spaces traveled by the ball from the start position
# (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.
# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the
# borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

# BFS. If can move in same direction, add to new_queue. Else check if solution, move perpendicular. Memoize visited
# locations and directions.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        rows, cols = len(maze), len(maze[0])
        distance = 0
        visited = set()
        dirns = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}
        perps = {"u": ("l", "r"), "d": ("l", "r"), "l": ("u", "d"), "r": ("u", "d")}
        queue = [(start[0], start[1], d) for d in dirns]

        while queue:

            new_queue = []

            while queue:

                r, c, dirn = queue.pop()
                if ((r, c, dirn)) in visited:
                    continue
                visited.add((r, c, dirn))

                dr, dc = dirns[dirn]
                if 0 <= r + dr < rows and 0 <= c + dc < cols and maze[r + dr][c + dc] == 0:
                    new_queue.append((r + dr, c + dc, dirn))
                else:
                    if [r, c] == destination:
                        return distance
                    perp = perps[dirn]
                    for new_dirn in perp:
                        queue.append((r, c, new_dirn))

            distance += 1
            queue = new_queue

        return -1

