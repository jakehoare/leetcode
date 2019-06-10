_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/fixed-point/
# Given an array A of distinct integers sorted in ascending order,
# return the smallest index i that satisfies A[i] == i.  Return -1 if no such i exists.

# Binary search the indices of the array.
# If a A[i] is greater than i then the fixed point must be to the left, so decrease right to i - 1.
# If a A[i] is leff than i then the fixed point must be to the right, so increase left to i + 1.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left, right = 0, len(A) - 1

        while left <= right:
            mid = (left + right) // 2
            if A[mid] == mid:
                return mid
            if A[mid] > mid:
                right = mid - 1
            else:
                left = mid + 1

        return -1
