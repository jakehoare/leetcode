_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/image-smoother/
# Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray
# scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself.
# If a cell has less than 8 surrounding cells, then use as many as you can.

# Iterate over M. For each cell, count and sum the neighbours (including self).
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(M), len(M[0])
        smoothed = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):

                nbors, total = 0, 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):

                        if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols:
                            continue
                        total += M[r + dr][c + dc]
                        nbors += 1

                smoothed[r][c] = total // nbors         # round down

        return smoothed