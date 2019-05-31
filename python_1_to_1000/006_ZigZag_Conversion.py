_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/zigzag-conversion/
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows.

# Build a list of chars for each row by tracking the direction of movement up or down and
# reversing direction at end rows.
# Time - O(n), use a list of chars and join instead of adding to immutable strings.
# Space - O(n)

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        zigzag = [[] for _ in range(numRows)]
        row = 0
        direction = -1      # -1 for up, +1 for down

        for c in s:
            zigzag[row].append(c)
            if row == 0 or row == numRows-1:    # change direction
                direction = -direction
            row += direction

        return "".join([c for r in zigzag for c in r])  # flatten list of lists
