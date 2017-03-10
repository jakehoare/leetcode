_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/design-tic-tac-toe/
# Design a Tic-tac-toe game that is played between two players on a n x n grid.
# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves is allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

# Arrays store the sums of each row and column, integers store the sums of the diagonals.  Convert player to +/-1 and
# increment sum of row, col and potentially diagonals.  Check if any of row, col or diagonal has absolute sum of n.
# Time - O(n) for constructor and to O(1) for move()
# Space - O(n)

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows, self.cols = [0 for _ in range(n)], [0 for _ in range(n)]
        self.d_up, self.d_down = 0, 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        n = len(self.rows)
        score = (2 * player) - 3    # convert player to -1 or +1

        self.rows[row] += score
        self.cols[col] += score
        if abs(self.rows[row]) == n or abs(self.cols[col]) == n:
            return player

        if row == col:
            self.d_up += score
            if abs(self.d_up) == n:
                return player
        if row + col == n - 1:
            self.d_down += score
            if abs(self.d_down) == n:
                return player

        return 0
