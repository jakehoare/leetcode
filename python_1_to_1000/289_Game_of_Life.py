_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/game-of-life/
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules::
#   Any live cell with fewer than two live neighbors dies, as if caused by under-population.
#   Any live cell with two or three live neighbors lives on to the next generation.
#   Any live cell with more than three live neighbors dies, as if by over-population..
#   Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state.

# For each cell in current board count neighbours and if 3 or 2 and cell is alive, set the second bit to signify
# that in the next timestep the cell will be alive.  Then update the fisrt bit to the second bit.
# Time - O(m * n)
# Space - O(1)

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                nbors = self.count_neighbours(r, c, board)
                if nbors == 3 or (board[r][c] and nbors == 2):
                    board[r][c] += 2    # set second bit so signify next status is alive

        for r in range(rows):
            for c in range(cols):
                board[r][c] >>= 1       # 2nd bit determines next status


    def count_neighbours(self, r, c, board):

        count = 0
        for row_offset in range(-1, 2):
            for col_offset in range(-1, 2):

                if row_offset == col_offset == 0:
                    continue
                if 0 <= r+row_offset < len(board) and 0 <= c+col_offset < len(board[0]):
                    count += board[r+row_offset][c+col_offset] % 2      # 1st bit defines current status

        return count
