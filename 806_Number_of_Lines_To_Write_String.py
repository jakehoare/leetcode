_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-lines-to-write-string/
# We are to write the letters of a given string S, from left to right into lines.
# Each line has maximum width 100 units, and if writing a letter would cause the width of the line to exceed 100 units,
# it is written on the next line. We are given an array widths, an array where widths[0] is the width of 'a',
# widths[1] is the width of 'b', ..., and widths[25] is the width of 'z'.
# Now answer two questions: how many lines have at least one character from S,
# and what is the width used by the last such line? Return your answer as an integer list of length 2.

# Track the current line number and its width. Start with zero lines of length 100 to handle empty S.
# For each char in S, add it to the current line if there is room, else start another line.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        line, width = 0, 100            # line number and width

        for c in S:

            c_length = widths[ord(c) - ord("a")]

            if width + c_length > 100:  # cannot fit c on this line, start a new line
                line += 1
                width = 0

            width += c_length

        return [line, width]