_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/transform-to-chessboard/
# An N x N board contains only 0s and 1s. In each move, you can swap any 2 rows with each other,
# or any 2 columns with each other.
# What is the minimum number of moves to transform the board into a "chessboard" - a board where no 0s and no 1s
# are 4-directionally adjacent? If the task is impossible, return -1.

# If two rows are identical, then swapping columns does not change this. The solution has two types of row and since we
# cannot change the number of row types by swapping columns, the board must only have two types of row initially.
# The two types of row must be opposite and differ in their number of zeros by len(board) % 1.
# If len(board) is odd, find the type with the most zeros and count the moves to convert it to the required target
# beginning with zero. Else find the minimum steps to either the target beginning with zero or one.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)

        rows = {tuple(row) for row in board}    # set of row tuples
        cols = set(zip(*board))                 # transpose, converts to column tuples

        moves = 0
        for patterns in [rows, cols]:           # process rows then columns

            if len(patterns) != 2:              # 2 types of row or column
                return -1

            p1, p2 = list(patterns)

            zero_p1, zero_p2 = sum(x == 0 for x in p1), sum(x == 0 for x in p2)
            if abs(zero_p1 - zero_p2) != n % 2 or not all(x ^ y for x, y in zip(p1, p2)):   # opposites
                return -1

            p = p1 if zero_p1 > zero_p2 else p2 # choose pattern with most zeros
            p_moves = sum(x != y for x, y in zip(p, [0, 1] * ((n + 1) // 2)))
            if n % 2 == 0:                      # need to check steps to both targets for even board lengths
                p_moves = min(p_moves, sum(x != y for x, y in zip(p, [1, 0] * ((n + 1) // 2))))

            moves += p_moves // 2               # each swap corrects the position of 2 items

        return moves
