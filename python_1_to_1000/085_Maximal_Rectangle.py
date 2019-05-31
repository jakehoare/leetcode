_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximal-rectangle/
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

# For each row build a 'histogram' of the number of 1s above and including each column.  Then proceed as for problem 084
# and pop a column off the stack whenever its 2 boundaries are lower.
# Time - O(m*n)
# Space - O(n)

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        max_area = 0
        heights = [0] * cols

        for row in range(rows):

            heights = [heights[i]+1 if matrix[row][i]=='1' else 0 for i in range(cols)]
            heights.append(0)
            stack = [0]

            for col in range(1, len(heights)):
                while stack and heights[col] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    if not stack:
                        width = col
                    else:
                        width = col - stack[-1] - 1
                    max_area = max(max_area, height * width)

                stack.append(col)

        return max_area
