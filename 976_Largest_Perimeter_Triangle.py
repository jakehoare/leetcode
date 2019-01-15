_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/largest-perimeter-triangle/
# Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area,
# formed from 3 of these lengths.
# If it is impossible to form any triangle of non-zero area, return 0.

# For each side s, if the sum of the next 2 smaller sides is lower then a triangle can be formed.
# If no such triangle can be formed with s as the longest side, then other shorter sides cannot form a triangle.
# When the sides are sorted by decreasing length, the first such triangle has the largest perimeter.
# Time - O(n log n)
# Space - O(n)

class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort(reverse=True)

        for i, side in enumerate(A[:-2]):
            if side < A[i + 1] + A[i + 2]:
                return side + A[i + 1] + A[i + 2]

        return 0