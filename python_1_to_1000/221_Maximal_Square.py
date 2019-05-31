_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximal-square/
# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# For each cell find the largest square with that cell at the bottom right by dynamic programming.
# If cell == '1' then it extends the squares with bottom right cells to the left, above and above-left.  Take the min
# of these 3 squares that are extended.
# Time - O(m * n)
# Space - O(n)

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        max_side = 0
        square_sides = [0] * cols       # largest square side with cell in each col as bottom right

        for r in range(rows):

            new_square_sides = [int(matrix[r][0])] + [0 for _ in range(cols-1)]

            for c in range(1, cols):
                if matrix[r][c] == '1':
                    new_square_sides[c] = 1 + min(new_square_sides[c-1], square_sides[c], square_sides[c-1])

            max_side = max(max_side, max(new_square_sides))
            square_sides = new_square_sides

        return max_side**2