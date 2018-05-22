_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reshape-the-matrix/
# In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different
# size but keep its original data.
# You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the
# row number and column number of the wanted reshaped matrix, respectively.
# The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order
# as they were. If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix.
# Otherwise, output the original matrix.

# Iterate over nums, appending elements to reshape and starting new rows when full.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        rows, cols = len(nums), len(nums[0])
        if rows * cols != r * c:            # return if different number of elements
            return nums

        reshaped = [[]]

        for i in range(rows):
            for j in range(cols):

                if len(reshaped[-1]) == c:  # end of column, start new column
                    reshaped.append([])
                reshaped[-1].append(nums[i][j])

        return reshaped