_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/partition-array-into-disjoint-intervals/
# Given an array A, partition it into two (contiguous) subarrays left and right so that:
# Every element in left is less than or equal to every element in right.
# left and right are non-empty.
# left has the smallest possible size.
# Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

# Iterate along array tracking the maximum number in left partition, its index and the overall maximum number.
# If the next number is less than the maximum in the left partition, it must extend the left partition. When the left
# partition is extended, its maximum becomes the overall maximum.
# Time - O(n)
# Space - O(1)

class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        last_left = 0
        max_left = max_overall = A[0]

        for i, num in enumerate(A[1:], 1):

            max_overall = max(max_overall, num)

            if num < max_left:  # smaller must be included in left
                last_left = i
                max_left = max_overall

        return last_left + 1