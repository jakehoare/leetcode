_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/valid-sudoku/
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

# Create a set of digits seen in each row, column and box.  False if any duplicates.
# Time - O(n^2) for board of side n
# Space - O(n)

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        size = 9
        digits = {str(i) for i in range(1,10)}
        rows = [set() for _ in range(size)]
        cols = [set() for _ in range(size)]
        boxes = [set() for _ in range(size)]

        for r in range(size):
            for c in range(size):

                digit = board[r][c]
                if digit == '.':
                    continue

                if digit not in digits:
                    return False

                box = (size//3) * (r // (size//3)) + (c // (size//3))
                if digit in rows[r] or digit in cols[c] or digit in boxes[box]:
                    return False
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box].add(digit)

        return True