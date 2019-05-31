_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/lonely-pixel-i/
# Given a picture consisting of black and white pixels, find the number of black lonely pixels.
# The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels
# respectively. A black lonely pixel is character 'B' that located at a specific position where the same row and same
# column don't have any other black pixels.

# Record black pixels in each row and counts by column. Then for each row with 1 pixel, check if that column also
# has 1 pixel.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        pixels = 0
        rows, cols = len(picture), len(picture[0])

        col_counts = [0 for _ in range(cols)]  # black pixels per column
        row_pixels = [[] for _ in range(rows)]  # black pixels indices by row

        for r in range(rows):
            for c in range(cols):
                if picture[r][c] == "B":
                    col_counts[c] += 1
                    row_pixels[r].append(c)

        for r in range(rows):
            if len(row_pixels[r]) == 1:
                c = row_pixels[r][0]
                if col_counts[c] == 1:
                    pixels += 1

        return pixels
