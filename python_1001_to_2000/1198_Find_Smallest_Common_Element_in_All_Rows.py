_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-smallest-common-element-in-all-rows/
# Given a matrix mat where every row is sorted in increasing order, return the smallest common element in all rows.
# If there is no common element, return -1.

# Create a set of all elements from the first row.
# For each other row, retain common elements from that row and all previous rows.
# Time - O(mn)
# Space - O(m)

class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        candidates = set(mat[0])

        for row in mat[1:]:
            candidates &= set(row)

        return min(candidates) if candidates else -1
