_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/lonely-pixel-ii/
# Given a picture consisting of black and white pixels, and a positive integer N, find the number of black pixels
# located at some specific row R and column C that align with all the following rules:
# Row R and column C both contain exactly N black pixels.
# For all rows that have a black pixel at column C, they should be exactly the same as row R
# The picture is represented by a 2D char array consisting of 'B' and 'W' pixels.

# Iterate over picture, for each row if contains N black pixels add to row_strings counter. Also count black pixels
# by column. Then if a row does not have a count of N each black pixel either cannot have col_count of N or is not from
# an identical row. Else count black pixels from all cols with countof N.
# Time - O(mn)
# Space - O(mn) 

from collections import defaultdict

class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        pixels = 0
        rows, cols = len(picture), len(picture[0])

        col_counts = [0 for _ in range(cols)]   # black pixels per column
        row_strings = defaultdict(int)          # string representation of row mapped to its frequency

        for r in range(rows):
            row_count = 0                       # black pixels in this row
            for c in range(cols):
                if picture[r][c] == "B":
                    col_counts[c] += 1
                    row_count += 1
            if row_count == N:
                row_strings["".join(picture[r])] += 1

        for row_string in row_strings:
            if row_strings[row_string] == N:  # else not all rows with black pixel in a given col are identical
                for i, col in enumerate(row_string):
                    if col == "B" and col_counts[i] == N:
                        pixels += N

        return pixels