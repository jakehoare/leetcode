_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/
# Given a 01 matrix M, find the longest line of consecutive one in the matrix.
# The line could be horizontal, vertical, diagonal or anti-diagonal.

# Dynamic programming. Iterate over matrix, if cell == 1 update longest line in each of 4 directions based on
# longest lines to cells on left and in previous row.
# Time - O(mn)
# Space - O(n), number of columns

class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0

        rows, cols = len(M), len(M[0])
        max_len = 0

        # row_dp[i] is a list of be longest line ending at column i on the current row
        # for horizontal, vertical, descending and ascending diagonal lines
        previous_dp = [[0 for _ in range(4)] for c in range(cols)]

        for r in range(rows):
            row_dp = []

            for c in range(cols):

                if M[r][c] == 0:  # cannot extend any lines
                    row_dp.append([0 for _ in range(4)])
                    continue

                row_dp.append([1 for _ in range(4)])  # default line length of this cell

                if c != 0:
                    row_dp[-1][0] += row_dp[-2][0]  # horizontal
                row_dp[-1][1] += previous_dp[c][1]  # vertical
                if c != 0:                          # descending diagonal
                    row_dp[-1][2] += previous_dp[c - 1][2]
                if c != cols - 1:                   # ascending diagonal
                    row_dp[-1][3] += previous_dp[c + 1][3]

                max_len = max(max_len, max(row_dp[-1]))

            previous_dp = row_dp

        return max_len
