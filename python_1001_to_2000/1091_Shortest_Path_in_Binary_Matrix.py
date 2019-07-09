_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shortest-path-in-binary-matrix/
# In an N by N square grid, each cell is either empty (0) or blocked (1).
# A clear path from top-left to bottom-right has length k if and only if it is composed of
# cells C_1, C_2, ..., C_k such that:
# Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
# C_1 is at location (0, 0) (ie. has value grid[0][0])
# C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
# If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
# Return the length of the shortest such clear path from top-left to bottom-right.
# If such a path does not exist, return -1.

# Bidirectional breadth-first search.
# Maintain frontiers of valid (within grid), empty cells.
# Expand the smaller frontier by visiting all neighbours.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:  # front and back frontiers only contain empty cells
            return -1
        front, back = {(0, 0)}, {(n - 1, n - 1)}
        visited = set()
        path = 0

        while front and back:
            path += 1
            if front & back:                            # frontiers intersect
                return path
            if len(front) > len(back):
                front, back = back, front
            new_front = set()

            for r, c in front:
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):               # dr == dc == 0 is visited
                        if r + dr < 0 or r + dr >= n:
                            continue
                        if c + dc < 0 or c + dc >= n:
                            continue
                        if grid[r + dr][c + dc] == 1:
                            continue
                        new_front.add((r + dr, c + dc))

            visited |= front
            new_front -= visited
            front = new_front

        return -1
