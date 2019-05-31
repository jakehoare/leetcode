_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/surrounded-regions/
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# All edge cells containing 'O' and their adjoining 'O' cannot be surrounded.  Temporarily flag these cells, by depth-
# first search. Then convert all unflagged 'O' (that can be surrounded) to 'X'.
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

        rows, cols = len(board), len(board[0])

        to_expand = []              # stack of cells to be checked

        for row in range(rows):     # add all edge cells to stack
            to_expand += [(row, 0), (row, cols - 1)]
        for col in range(1, cols-1):
            to_expand += [(0, col), (rows - 1, col)]

        while to_expand:            # if cell contains 'O', change to temporary 'T' and add neighbours to stack
            row, col = to_expand.pop()
            if 0 <= row < rows and 0 <= col < cols and board[row][col] == 'O':
                board[row][col] = 'T'
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    to_expand.append((row + dr, col + dc))

        for row in range(rows):     # change all 'T' back to 'O' and all 'O' to 'X'
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'T':
                    board[row][col] = 'O'