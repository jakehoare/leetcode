_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/alphabet-board-path/
# On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].
# Here, board = ["abcde",
#                "fghij",
#                "klmno",
#                "pqrst",
#                "uvwxy",
#                "z"].
# We may make the following moves:
# 'U' moves our position up one row, if the position exists on the board;
# 'D' moves our position down one row, if the position exists on the board;
# 'L' moves our position left one column, if the position exists on the board;
# 'R' moves our position right one column, if the position exists on the board;
# '!' adds the character board[r][c] at our current position (r, c) to the answer.
# (Here, the only positions that exist on the board are positions with letters on them.)
# Return a sequence of moves that makes our answer equal to target in the minimum number of moves.
# You may return any path that does so.

# Track the current location and for each char, find the target location.
# Move left and up before right and down so we do not visit any other columns on the last row.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        def location(char):     # return (row, col) of cher on the board.
            val = ord(char) - ord("a")
            return divmod(val, 5)

        result = []
        row, col = 0, 0
        for char in target:
            r, c = location(char)
            if c < col:
                result += ["L"] * (col - c)
            if r < row:
                result += ["U"] * (row - r)
            if c > col:
                result += ["R"] * (c - col)
            if r > row:
                result += ["D"] * (r - row)

            row, col = r, c
            result.append("!")

        return "".join(result)
