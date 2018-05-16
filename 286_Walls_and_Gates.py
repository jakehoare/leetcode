_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/walls-and-gates/
# You are given a m x n 2D grid initialized with these three possible values.
#   -1 - A wall or an obstacle.
#   0 - A gate.
#   INF - Infinity means an empty room. We use the value 2**31 - 1 = 2147483647 to represent INF.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# Multidirectional BFS. Frontier initially contains all gates.  For each room in frontier update any surrounding
# rooms with infinite distance and add them to frontier. Expands in concentric circles around gates.
# DFS or BFS from each gate in turn can result in repeatedly updating rooms and greater time complexity.
# Time - O(m * n), each cell visited once
# Space - O(m * n) for queue

from collections import deque

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return

        INF = 2 ** 31 - 1
        rows, cols = len(rooms), len(rooms[0])
        frontier = deque([(r, c) for r in range(rows) for c in range(cols) if rooms[r][c] == 0])

        while frontier:
            row, col = frontier.popleft()
            for i, j in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if i >= 0 and i < rows and j >= 0 and j < cols:
                    if rooms[i][j] == INF:
                        rooms[i][j] = rooms[row][col] + 1
                        frontier.append((i, j))