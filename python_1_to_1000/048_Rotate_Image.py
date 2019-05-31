_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/rotate-image/
# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).

# Number of layer to rotate is n//2.  For each item along the top side of each layer, save as temp and
# move in the item from the next side, repeating until temp is put into the last side.
# Alternatively - matrix[:] = list(map(list, zip(*matrix[::-1]))).  Reverse the order of row, unpack,
# zip and convert back to lists.
# Time - O(n^2)
# Space - O(1)

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        layers = n//2

        for layer in range(layers):
            for i in range(layer, n - layer - 1):
                temp = matrix[layer][i]
                matrix[layer][i] = matrix[n - 1 - i][layer]
                matrix[n - 1 - i][layer] = matrix[n - 1 - layer][n - 1- i]
                matrix[n - 1 - layer][n - 1 - i] = matrix[i][n - 1 - layer]
                matrix[i][n - 1 - layer] = temp
