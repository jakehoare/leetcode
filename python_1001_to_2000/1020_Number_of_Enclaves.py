_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-enclaves/
# Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)
# A move consists of walking from one land square 4-directionally to another land square,
# or off the boundary of the grid.
# Return the number of land squares in the grid for which we cannot walk off the boundary of the grid
# in any number of moves.

# For each cell of the grid, explore the connected (land) cells with depth-first search.
# A flag indicates whether any connected cell touches the edge of the grid, so the island is not an enclave.
# Set the value of each cell visited to zero to avoid repetition.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        rows, cols = len(A), len(A[0])
        result = 0
        self.edge = False       # flag indicating whether current group of cells touches an edge of the grid

        def enclave(r, c):      # return count of enclave cells, or zero if not an enclave
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0
            if A[r][c] != 1:
                return 0

            if r == 0 or c == 0 or r == rows - 1 or c == cols - 1:
                self.edge = True
            A[r][c] = 0
            count = 1
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:   # recursively add all neighbours
                count += enclave(r + dr, c + dc)
            return count if not self.edge else 0                # return 0 if not an enclave

        for r in range(rows):
            for c in range(cols):
                self.edge = False                               # reset flag for each cell
                result += enclave(r, c)

        return result
