_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/01-matrix/
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.

# Queue of cells with known distances, initially 0 cells. 1 cells are set max possible distance. For each cell in\
# frontier, reduce distance of all neighbours to 1 + frontier distance and add neighbours back to queue.
# Alternatively maintain set of cells with unknown distances. If any cell with unknown distance is next to a known
# cell then set distance. May iterate over unknowns many times but faset in practice.
# Time - O(mn)
# Space - O(mn)

from collections import deque

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(matrix), len(matrix[0])
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        frontier = deque()  # tuples of matrix coordinates

        max_dist = max(rows, cols)
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    matrix[r][c] = max_dist
                else:
                    frontier.append((r, c))

        while frontier:
            r, c = frontier.popleft()
            for dr, dc in deltas:
                if 0 <= r + dr < rows and 0 <= c + dc < cols and matrix[r][c] + 1 < matrix[r + dr][c + dc]:
                    matrix[r + dr][c + dc] = matrix[r][c] + 1
                    frontier.append((r + dr, c + dc))

        return matrix


class Solution2(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(matrix), len(matrix[0])
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        unknown = set()  # tuples of matrix coordinates where distance to nearest zero is unknown

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    unknown.add((r, c))

        while unknown:
            new_unknown = set()
            for r, c in unknown:
                for dr, dc in deltas:
                    if 0 <= r + dr < rows and 0 <= c + dc < cols and (r + dr, c + dc) not in unknown:
                        matrix[r][c] = matrix[r + dr][c + dc] + 1
                        break
                else:  # no known neighbours
                    new_unknown.add((r, c))

            unknown = new_unknown

        return matrix