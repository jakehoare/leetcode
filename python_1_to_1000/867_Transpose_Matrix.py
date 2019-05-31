_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/transpose-matrix/
# Given a matrix A, return the transpose of A.
# The transpose of a matrix is the matrix flipped over it's main diagonal,
# switching the row and column indices of the matrix.

# Explode A into rows, which are zipped together with the ith element of each row (i.e. column i) being combined in
# each tuple of the result.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return zip(*A)