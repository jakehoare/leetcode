_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/flipping-an-image/
# Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
# For example, inverting [0, 1, 1] results in [1, 0, 0].

# Reverse each row set each value to 1 - value so 0 becomes 1 and 1 becomes 0.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []

        for row in A:
            result.append([1 - val for val in reversed(row)])

        return result
