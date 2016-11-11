_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/pascals-triangle/
# Given numRows, generate the first numRows of Pascal's triangle.

# Next row is sum of consecutive pairs of items from previous row.
# Time - O(n**2)
# Space - O(n**2)

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        pascal = [[1]]

        for i in range(1, numRows):

            pascal.append([1])
            for num1, num2 in zip(pascal[-2][:-1], pascal[-2][1:]):
                pascal[-1].append(num1 + num2)
            pascal[-1].append(1)

        return pascal
