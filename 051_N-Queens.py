_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/n-queens/
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# Each solution contains a distinct board configuration of the n-queens' placement,
# where 'Q' and '.' both indicate a queen and an empty space respectively.

# For each column, place a queen in each possible row that does not conflict with an existing queen.
# Time - O(n^2 * n!), n possible rows for first col, n-1 for second ... etc.  each result size n^2
# Space - O(n^2 * n!)

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        partials = [[]]
        for col in range(n):
            new_partials = []
            for partial in partials:
                for row in range(n):
                    if not self.conflict(partial, row):
                        new_partials.append(partial + [row])
            partials = new_partials

        results = []
        for partial in partials:
            result = [['.'] * n for _ in range(n)]
            for col, row in enumerate(partial):
                result[row][col] = 'Q'
            for row in range(n):
                result[row] = ''.join(result[row])
            results.append(result)

        return results

    def conflict(self, partial, new_row):
        for col, row in enumerate(partial):
            if new_row == row:
                return True
            col_diff = len(partial) - col
            if row + col_diff == new_row or row - col_diff == new_row:
                return True
        return False
