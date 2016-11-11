_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/triangle/
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# Bottom-ip dynamic programming.  Min path is value of that element + min of the 2 paths to elements below.
# Time - O(n**2) for triangle height n since all elements visited
# Space - O(1), modifies input data

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for row in range(len(triangle)-2, -1, -1):

            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row+1][col], triangle[row+1][col+1])

        return triangle[0][0]