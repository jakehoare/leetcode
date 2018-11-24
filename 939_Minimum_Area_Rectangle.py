_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-area-rectangle/
# Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points,
# with sides parallel to the x and y axes.
# If there isn't any rectangle, return 0.

# Create a map of all the column values at each row value.
# If there are more columns than rows, then we swap this map so it is from each column value to a list of row values.
# Sort the row values. For each row, sort the column values. For each pair of columns in that row, if the column
# pair has appeared in a previous row then we have a rectangle.
# Update the mapping with each column pair to it's most recent row.
# Time - O(max(m, n) * min(m, n) ** 2) since we swap to ensure the inner loop over pairs is over the shorter list
# Space - O(mn)

from collections import defaultdict

class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        rows, cols = set(), set()               # sets of unque row and column values
        for r, c in points:
            rows.add(r)
            cols.add(c)

        row_to_cols = defaultdict(list)         # map from a row to the list of columns
        if len(rows) > len(cols):
            for r, c in points:
                row_to_cols[r].append(c)
        else:                                   # swap map to be from column to list of rows
            for r, c in points:
                row_to_cols[c].append(r)

        result = float("inf")

        col_pair_to_row = {}                    # map from pair of column values to a row

        for r in sorted(row_to_cols):

            columns = sorted(row_to_cols[r])

            for i, c1 in enumerate(columns[:-1]):
                for c2 in columns[i + 1:]:

                    if (c1, c2) in col_pair_to_row:     # previous row has this column pair
                        result = min(result, (r - col_pair_to_row[c1, c2]) * (c2 - c1))
                    col_pair_to_row[c1, c2] = r

        return 0 if result == float('inf') else result