_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/squares-of-a-sorted-array/
# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number,
# also in sorted non-decreasing order.

# Left and right pointers mark next elements to be squared. Add the larger square to the result and move pointers
# until they cross.
# Time - O(n)
# Space - O(n)

class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(A) - 1
        result = []

        while left <= right:
            if abs(A[left]) > abs(A[right]):
                result.append(A[left] * A[left])
                left += 1
            else:
                result.append(A[right] * A[right])
                right -= 1

        return result[::-1]     # reverse to decreasing order
