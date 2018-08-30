_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/buddy-strings/
# Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that
# the result equals B.

# We can always set all the bits in the first column by either flipping rows that start with zero, or flipping all
# rows that start with one then flipping the whole column. These two cases result in the bits in the other columns
# being opposites. In either case we can flip each column so that the most common bit in that column is set.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        rows, cols = len(A), len(A[0])

        for r in range(rows):
            if A[r][0] == 0:                # row starts with zero
                for c in range(1, cols):    # flip all bits in the row
                    A[r][c] = 1 - A[r][c]

        score = rows * 2 ** (cols - 1)      # first columns bits are all set

        for c in range(1, cols):            # all other columns
            col_count = sum(A[r][c] for r in range(rows))       # count set bits in column
            best_col_count = max(col_count, rows - col_count)   # flip if required, so most common bit is set
            col_val = 2 ** ((cols - 1) - c)                     # score for a bit in this column
            score += col_val * best_col_count

        return score