_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/excel-sheet-column-title/
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
# For example:, 1 -> A, 2 -> B, 3 -> C, ..., 26 -> Z, 27 -> AA

# Generate characters starting with least significant by calculating remainder of division by 26.
# Time - O(log n)
# Space - O(log n)

from collections import deque

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        column = deque()    # faster than list for appendleft()
        while n > 0:
            n, output = divmod(n-1, 26)
            column.appendleft(output)

        return "".join([chr(i+ord('A')) for i in column])

