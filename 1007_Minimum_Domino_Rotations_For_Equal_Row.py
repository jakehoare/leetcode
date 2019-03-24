_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
# In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.
# A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.
# We may rotate the i-th domino, so that A[i] and B[i] swap values.
# Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.
# If it cannot be done, return -1.

# For each number from 1 to 6 inclusive, check if each domino has that number. There can be only one such number, or
# 2 numbers with an identical number of rotations, so we take the first such number found.
# For that number, either rotate for every A that is not the number, or every B that is not the number.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)

        for num in range(1, 7):
            if all(a == num or b == num for a, b in zip(A, B)):
                return min(n - A.count(num), n - B.count(num))

        return -1
