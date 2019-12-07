_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
# Tic-tac-toe is played by two players A and B on a 3 x 3 grid.
# Here are the rules of Tic-Tac-Toe:
# Players take turns placing characters into empty squares (" ").
# The first player A always places "X" characters, while the second player B always places "O" characters.
# "X" and "O" characters are always placed into empty squares, never on filled ones.
# The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# Given an array moves where each element is another array of size 2 corresponding to the
# row and column of the grid where they mark their respective character in the order in which A and B play.
# Return the winner of the game if it exists (A or B),
# in case the game ends in a draw return "Draw",
# if there are still movements to play return "Pending".
# You can assume that moves is valid (It follows the rules of Tic-Tac-Toe),
# the grid is initially empty and A will play first.

# Denominate player A as 1 and player B as -1.
# Find the sum of move for each row, column and diagonal.
# If any line sums to 3 times the value of a player, that player wins.
# Else there is a draw if all squares are full, else pending.
# Time - O(1)
# Space - O(1)

class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        A, B = 1, -1
        player = A
        row_sums, col_sums = [0 for _ in range(3)], [0 for _ in range(3)]
        up_diag, down_diag = 0, 0       # sums of moves along diagonals

        for r, c in moves:              # add move to sums for each line
            row_sums[r] += player
            col_sums[c] += player
            if r == c:
                up_diag += player
            if r + c == 2:
                down_diag += player

            player = -player            # change player

        lines = row_sums + col_sums + [up_diag, down_diag]
        if any(line == 3 * A for line in lines):
            return "A"
        if any(line == 3 * B for line in lines):
            return "B"
        return "Draw" if len(moves) == 9 else "Pending"

