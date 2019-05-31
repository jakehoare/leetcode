_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/pascals-triangle-ii/
# Given an index k, return the kth row of the Pascal's triangle.

# Next row is sum of consecutive pairs of previous row.
# Time - O(n**2)
# Space - O(n)

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in range(rowIndex):
            row = [1] + [row[i]+row[i+1] for i in range(len(row)-1)] + [1]
        return row