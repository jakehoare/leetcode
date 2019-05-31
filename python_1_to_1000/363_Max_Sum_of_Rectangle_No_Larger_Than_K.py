_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/max-sum-of-sub-matrix-no-larger-than-k/
# Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that
# its sum is no larger than k.

# For each column forming the left edge of the rectangle, calculate cumulative row_sums for each column at the right
# edge of the rectangle. For each right edge column, iterate over rows and maintain a sorted list of the sum of the
# cells between those columns for each row. For each row, find the value in the list that makes a rectangle with sum
# not more than k. Insert cumulative row sum into list.
# Alternatively use skip list or self-balancing tree to maintain sorted list.
# Time - O(n**2 * m**2)
# Space - O(m)

import bisect

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        max_sum = float("-inf")

        for i in range(cols):
            row_sums = [0 for _ in range(rows)]

            for j in range(i, cols):
                sorted_sums = [0]   # sum of rows between these columns
                all_row_sum = 0     # sum of cols i to j (inclusive), rows 0 to r (inclusive)

                for r in range(rows):
                    row_sums[r] += matrix[r][j]
                    all_row_sum += row_sums[r]

                    larger = bisect.bisect_left(sorted_sums, all_row_sum - k)   #
                    if larger != len(sorted_sums):
                        if all_row_sum - sorted_sums[larger] == k:  # cannot improve, early return
                            return k
                        max_sum = max(max_sum, all_row_sum - sorted_sums[larger])

                    bisect.insort_left(sorted_sums, all_row_sum)        # insert all_row_sum in sorted list

        return max_sum
