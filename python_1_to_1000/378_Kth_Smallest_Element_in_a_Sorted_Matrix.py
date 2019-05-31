_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest
# element in the matrix.  Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# Maintain a heap of frontier numbers to be checked.  Remove smallest and add next smallest column (if not end) and
# if first column also add next smallest row (if any) to heap.
# If k if is more than half the size of the matrix, look for m * n - k + 1th largest.
# Time - O(m * n)
# Space - O(m + n)

import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # start at opposite corner if more than half
        rows, cols = len(matrix), len(matrix[0])

        if k > (rows * cols) // 2:
            back = True
            k = rows * cols - k + 1
            frontier = [(-matrix[rows - 1][cols - 1], rows - 1, cols - 1)]
        else:
            back = False
            frontier = [(matrix[0][0], 0, 0)]

        while k:
            val, r, c = heapq.heappop(frontier)
            k -= 1
            if not back:
                if c != len(matrix[0]) - 1:
                    heapq.heappush(frontier, (matrix[r][c + 1], r, c + 1))
                if c == 0 and r != len(matrix) - 1:
                    heapq.heappush(frontier, (matrix[r + 1][c], r + 1, c))
            else:
                if c != 0:
                    heapq.heappush(frontier, (-matrix[r][c - 1], r, c - 1))
                if c == cols - 1 and r != 0:
                    heapq.heappush(frontier, (-matrix[r - 1][c], r - 1, c))

        return -val if back else val
