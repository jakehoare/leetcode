_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/candy-crush/
# This question is about implementing a basic elimination algorithm for Candy Crush.
# Given a 2D integer array board representing the grid of candy, different positive integers board[i][j] represent
# different types of candies. A value of board[i][j] = 0 represents that the cell at position (i, j) is empty. The
# given board represents the state of the game following the player's move. Now, you need to restore the board to a
# stable state by crushing candies according to the following rules:
# If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same
# time - these positions become empty.
# After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these
# candies will drop until they hit a candy or bottom at the same time. (No new candies will drop outside the
# top boundary.)
# After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
# If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.
# You need to perform the above rules until the board becomes stable, then return the current board.

# Iterate over board setting to_crush for rows or columns of 3 identical (but not empty) candies. If nothing found,
# return board. For each column, create a new empty column and fill from bottom up with candies that are not crushed.
# Time - O((mn)**2), mn per cycle with mn // 3 max cycles.
# Space - O(mn)

class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(board), len(board[0])

        while True:

            stable = True
            to_crush = [[False for _ in range(cols)] for _ in range(rows)]      # flag which cells to crush

            for c in range(cols):
                for r in range(rows):
                    # check vertical
                    if r < rows - 2 and board[r][c] == board[r + 1][c] == board[r + 2][c] and board[r][c] != 0:
                        to_crush[r][c] = to_crush[r + 1][c] = to_crush[r + 2][c] = True
                        stable = False
                    # check horizontal
                    if c < cols - 2 and board[r][c] == board[r][c + 1] == board[r][c + 2] and board[r][c] != 0:
                        to_crush[r][c] = to_crush[r][c + 1] = to_crush[r][c + 2] = True
                        stable = False

            if stable:  # nothing to crush
                return board

            for c in range(cols):
                new_col = [0 for _ in range(rows)]
                new_r = rows - 1
                for r in range(rows - 1, -1, -1):       # from bottom upwards
                    if not to_crush[r][c]:
                        new_col[new_r] = board[r][c]    # add to new_col if not crushed
                        new_r -= 1                      # decrement new_r
                if new_r != -1:                         # column has changed so update board
                    for r in range(rows):
                        board[r][c] = new_col[r]

