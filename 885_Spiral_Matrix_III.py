_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/spiral-matrix-iii/
# On a 2 dimensional grid with R rows and C columns, we start at (r0, c0) facing east.
# Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the
# grid is at the last row and column.
# Now, we walk in a clockwise spiral shape to visit every position in this grid.
# Whenever we would move outside the boundary of the grid, we continue our walk outside the grid
# (but may return to the grid boundary later.)
# Eventually, we reach all R * C spaces of the grid.
# Return a list of coordinates representing the positions of the grid in the order they were visited.

# Move in a spiral until all cells of the grid have been visited. Step along each side, then turn to next direction.
# Each cell visited within the grid is appended to the result. Spiral has two sides of the same length, then two sides
# of length + 1, etc.
# Time - O(max(m, n)**2)
# Space - O(mn)

class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]      # change in r and c foa move in each direction
        r, c = r0, c0
        direction = 0
        result = [[r0, c0]]
        side = 1                                        # current length of side of spiral

        while len(result) < R * C:

            dr, dc = moves[direction]

            for _ in range(side):                       # step along the side
                r += dr
                c += dc
                if 0 <= r < R and 0 <= c < C:           # append to result if within bounds of grid
                    result.append([r, c])

            direction = (direction + 1) % 4             # next direction
            dr, dc = moves[direction]

            for _ in range(side):
                r += dr
                c += dc
                if 0 <= r < R and 0 <= c < C:
                    result.append([r, c])

            direction = (direction + 1) % 4
            side += 1                                   # after 2 sides of spiral, increase side length

        return result