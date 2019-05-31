_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/best-meeting-point/
# A group of two or more people wants to meet and minimize the total travel distance.
# You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group.
# Calculated the minimum travel using Manhattan Distance,

# Create sorted lists of row and column indices of people.  Because dimensions are independent for Manhattan distance,
# rows and cols can be optimised separately.  Optimal meet is median of sorted indices (or anywhere between median pair
# if even number).  To reach a meet between a pair of points takes distance of points separation if meet is between
# points, else greater distance if meet is not between points.  Hence optimal meet is between the most pairs of
# points, which is the median.
# Time - O((m*n) + nlogn)
# Space - O(m * n) if all cells contain people

class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = [], []

        for r in range(len(grid)):      # collect rows in sorted order
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    rows.append(r)
                    cols.append(c)

        cols.sort()     # potentially better to collect cols in separate loop O(m*n) rather than sort in O(n log n)
        dist = 0

        left, right = 0, len(rows)-1    # increment distance by separation of outer pair of rows
        while left < right:
            dist += (rows[right] - rows[left])
            left += 1
            right -= 1

        left, right = 0, len(cols)-1    # increment distance by separation of outer pair of cols
        while left < right:
            dist += (cols[right] - cols[left])
            left += 1
            right -= 1

        return dist