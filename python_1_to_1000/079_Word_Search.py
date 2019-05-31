_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/word-search/
# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
# or vertically neighboring. The same letter cell may not be used more than once.

# For each starting position, depth first search moving in all 4 directions and marking visited cells.
# Time - O(m * n * s), for each starting board position, try upto s characters
# Space - O(1)

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                if self.can_find(word, 0, board, r, c):
                    return True
        return False


    def can_find(self, word, i, board, r, c):

        if i >= len(word):              # nothing more of word to find
            return True
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):     # outside board
            return False
        if word[i] != board[r][c]:      # no match letter
            return False

        board[r][c] = '*'               # set this position so cannot be used again

        if (self.can_find(word, i+1, board, r+1, c) or self.can_find(word, i+1, board, r-1, c) or
                self.can_find(word, i+1, board, r, c+1) or self.can_find(word, i+1, board, r, c-1)):
            return True

        board[r][c] = word[i]           # if False, reset position to letter
        return False
