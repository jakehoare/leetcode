_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/battleships-in-a-board/
# Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are
# represented with '.'s. You may assume the following rules:
# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN
# (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
# At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.

# Sweep from top to bottom, left to right. New ship found if cell contains X and no X to left or above.
# Time - O(mn)
# Space - O(1)

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board or not board[0]:
            return 0

        rows, cols = len(board), len(board[0])
        ships = 0

        for r in range(rows):
            for c in range(cols):

                if board[r][c] == ".":
                    continue
                if r != 0 and board[r - 1][c] == "X":
                    continue
                if c != 0 and board[r][c - 1] == "X":
                    continue
                ships += 1

        return ships