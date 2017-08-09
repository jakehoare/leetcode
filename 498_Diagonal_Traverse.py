_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/diagonal-traverse/
# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown
# below. Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output:  [1,2,4,7,5,3,6,8,9]

# Boolan up_right determines direction of travel. Reverse when reach an edge.
# Time - O(mn)
# Space - O(1)

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        diagonal = []
        if not matrix or not matrix[0]:
            return diagonal

        rows, cols = len(matrix), len(matrix[0])
        up_right = True
        r, c = 0, 0

        while len(diagonal) < rows * cols:

            diagonal.append(matrix[r][c])

            if up_right:
                if c == cols - 1:   # right edge, move down 1 row
                    r += 1
                    up_right = False    # top edge, move across 1 column
                elif r == 0:
                    c += 1
                    up_right = False
                else:
                    r -= 1
                    c += 1

            else:
                if r == rows - 1:   # bottom edge, move across 1 column
                    c += 1
                    up_right = True
                elif c == 0:        # left edge, move down 1 row
                    r += 1
                    up_right = True
                else:
                    r += 1
                    c -= 1

        return diagonal