_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/the-maze/
# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down,
# left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
# Given the ball's start position, the destination and the maze, determine whether the ball can stop at the destination.
# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the
# borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

# DFS. Maintain queue of stopping points. For the next point, move in all 4 directions to find next stopping points.
# Store visisted points to avoid repetition.
# Time - O(m * n)
# Space - O(m * n)

class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        queue = [start]
        dirns = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visited = set()

        while queue:
            start_r, start_c = queue.pop()
            visited.add((start_r, start_c))

            for dr, dc in dirns:
                r, c = start_r, start_c     # move as far as possible
                while 0 <= r + dr < len(maze) and 0 <= c + dc < len(maze[0]) and maze[r + dr][c + dc] == 0:
                    r += dr
                    c += dc

                if (r, c) not in visited:
                    if [r, c] == destination:
                        return True
                    queue.append((r, c))    # DFS since add to end of queue

        return False