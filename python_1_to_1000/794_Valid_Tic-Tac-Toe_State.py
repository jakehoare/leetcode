_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/valid-tic-tac-toe-state/
# A Tic-Tac-Toe board is given as a string array board.
# Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.
# The board is a 3 x 3 array consisting of characters " ", "X", and "O".  The " " character represents an empty square.
# Here are the rules of Tic-Tac-Toe:
# Players take turns placing characters into empty squares (" ").
# The first player always places "X" characters, while the second player always places "O" characters.
# "X" and "O" characters are always placed into empty squares, never filled ones.
# The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.

# Count the number of Os and X and the number of winning rows of Os and Xs. Check only one winner and number of Os and
# Xs in the cases of either winner and no winner.
# Time - O(1) since board has fixed size of 3 x 3
# Space - O(1)

class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        counts, lines = [0, 0], [0, 0]          # counts of O and X, counts of lines of O and X

        for i, char in enumerate(("O", "X")):

            for j, row in enumerate(board):

                if row == char * 3:             # row lines
                    lines[i] += 1

                if board[0][j] == board[1][j] == board[2][j] == char:   # columns lines
                    lines[i] += 1

                for c in row:                   # counts
                    if c == char:
                        counts[i] += 1

            if board[0][0] == board[1][1] == board[2][2] == char:       # diagonal
                lines[i] += 1

            if board[2][0] == board[1][1] == board[0][2] == char:       # diagonal
                lines[i] += 1

        if lines[0] and lines[1]:                                       # cannot both win
            return False

        if lines[0] and counts[0] != counts[1]:                         # O wins, same number of each
            return False

        if lines[1] and counts[1] != counts[0] + 1:                     # X wins, one more X
            return False

        if counts[1] - counts[0] > 1 or counts[1] - counts[0] < 0:      # no winner
            return False

        return True