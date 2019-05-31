_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minesweeper/
# Let's play the minesweeper game (Wikipedia, online game)!
# You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an
# unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and
# all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
# finally 'X' represents a revealed mine.
# Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the
# board after revealing this position according to the following rules:
# If a mine ('M') is revealed, then the game is over - change it to 'X'.
# If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its
# adjacent unrevealed squares should be revealed recursively.
# If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8')
# representing the number of adjacent mines.
# Return the board when no more squares will be revealed.

# BFS. If mine, update and return. If blank count adjacent mines. If zero then recurse, else return count.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        r, c = click
        rows, cols = len(board), len(board[0])

        for row in range(rows):  # convert row string to list of chars
            board[row] = [col for col in board[row]]

        if board[r][c] == "M":  # return if mine
            board[r][c] = "X"
            return board

        def helper(r, c):
            if board[r][c] == "B":  # return unchanged if blank
                return

            mines = 0  # count adjacent mines
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == dc == 0:
                        continue
                    if 0 <= r + dr < rows and 0 <= c + dc < cols and board[r + dr][c + dc] == "M":
                        mines += 1

            if mines != 0:  # update with count or blank
                board[r][c] = str(mines)
                return
            board[r][c] = "B"

            for dr in [-1, 0, 1]:  # recurse
                for dc in [-1, 0, 1]:
                    if 0 <= r + dr < rows and 0 <= c + dc < cols:
                        helper(r + dr, c + dc)

        helper(r, c)
        return board