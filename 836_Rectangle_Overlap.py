_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/rectangle-overlap/
# A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner,
# and (x2, y2) are the coordinates of its top-right corner.
# Two rectangles overlap if the area of their intersection is positive.
# To be clear, two rectangles that only touch at the corner or edges do not overlap.
# Given two (axis-aligned) rectangles, return whether they overlap.

# Find overlap distance in x direction as the overlap of 2 line segments. If positive, check overlap in y direction.
# Time - O(1)
# Space - O(1)

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x_overlap = min(max(0, rec1[2] - rec2[0]), max(0, rec2[2] - rec1[0]))
        if x_overlap == 0:
            return False

        return min(max(0, rec1[3] - rec2[1]), max(0, rec2[3] - rec1[1])) > 0