_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/range-addition-ii/
# Given an m * n matrix M initialized with all 0's and several update operations.
# Operations are represented by a 2D array, and each operation is represented by an array with two positive
# integers a and b, which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.
# You need to count and return the number of maximum integers in the matrix after performing all the operations.

# Track the row and column edges of the part of the matrix containing the max integer. For each operation, update
# the row and column edges according to the minimum of the current values and the row and columns of the operation.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        max_r, max_c = m, n         # initially whole matrix contains max integer

        for r, c in ops:
            max_r = min(max_r, r)
            max_c = min(max_c, c)

        return max_r * max_c