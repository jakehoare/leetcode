_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/available-captures-for-rook/
# On an 8 x 8 chessboard, there is one white rook. There also may be empty squares, white bishops, and black pawns.
# These are given as characters 'R', '.', 'B', and 'p' respectively.
# Uppercase characters represent white pieces, and lowercase characters represent black pieces.
# The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south),
# then moves in that direction until it chooses to stop, reaches the edge of the board,
# or captures an opposite colored pawn by moving to the same square it occupies.
# Also, rooks cannot move into the same square as other friendly bishops.
# Return the number of pawns the rook can capture in one move.

# Find the coordinates of the rook. For each of the 4 directions, move until the edge of the board is reached, or a
# bishop, or a pawn. If a pawn is found first, increment the count of pawns that can be captured.
# Time - O(n**2) for board of size n
# Space - O(1)

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        SIZE = 8

        for r in range(SIZE):
            for c in range(SIZE):
                if board[r][c] == "R":
                    start_r, start_c = r, c
                    break

        pawns = 0
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            row, col = start_r, start_c
            while True:
                row += dr
                col += dc
                if row < 0 or row >= SIZE or col < 0 or col >= SIZE:
                    break
                if board[row][col] == "B":
                    break
                if board[row][col] == "p":
                    pawns += 1
                    break

        return pawns