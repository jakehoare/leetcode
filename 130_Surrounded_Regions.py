_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/surrounded-regions/
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# All edge cells containing 'O' adn their adjoining 'O' cannot be surrounded.  Temporarily flag these cell,
# then convert all unflagged 'O' to 'X'.
# Time - O(m * n)
# Space - O(m * n)

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        to_expand = []              # stack of cells to be checked

        for row in range(rows):     # add all edge cells to stack
            to_expand.append((row, 0))
            to_expand.append((row, cols-1))
        for col in range(1, cols-1):
            to_expand.append((0, col))
            to_expand.append((rows-1, col))

        while to_expand:            # if cell contains 'O', change to temporary 'T' and add neighbours to stack
            row, col = to_expand.pop()
            if 0 <= row < rows and 0 <= col < cols and board[row][col] == 'O':
                board[row][col] = 'T'
                to_expand.append((row+1, col))
                to_expand.append((row-1, col))
                to_expand.append((row, col+1))
                to_expand.append((row, col-1))

        for row in range(rows):     # change all 'T' back to 'O' and all 'O' to 'X'
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'T':
                    board[row][col] = 'O'