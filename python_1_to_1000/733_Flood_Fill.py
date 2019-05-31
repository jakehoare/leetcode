_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/flood-fill/
# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image
# (from 0 to 65535).
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value
# newColor, "flood fill" the image.
# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting
# pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with
# the same color as the starting pixel), etc. Replace the color of all of the aforementioned pixels with the newColor.
# At the end, return the modified image.

# Depth-first search. Find startColor or sr, sc. If this is the same as newColor, return image unchanged (or else
# the while loop may not terminate). Stack contains pixels to be explored. Pop the next unexplored cell and if a
# valid cell of startColor then change its colour and add neighbours to the stack.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        rows, cols = len(image), len(image[0])

        startColor = image[sr][sc]
        if startColor == newColor:
            return image

        stack = [(sr, sc)]

        while stack:

            r, c = stack.pop()

            if r < 0 or r >= rows or c < 0 or c >= cols:
                continue
            if image[r][c] != startColor:
                continue

            image[r][c] = newColor
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                stack.append((r + dr, c + dc))

        return image
