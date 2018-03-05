_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/rectangle-area/
# Find the total area covered by two rectilinear rectangles in a 2D plane.
# Each rectangle is defined by its bottom left corner (A, B) or (E, F) and top right corner (C, D) or (G, H).

# Calculate the left and right edges of horizontal overlap. Take the difference to get the x_overlap and similar for
# y_overlap. Subtract the overlap area from the sum of the areas of the two rectangles.
# Time - O(1)
# Space - O(1)

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        x_lhs = max(A, E)
        x_rhs = min(C, G)
        x_overlap = max(x_rhs - x_lhs, 0)

        y_lhs = max(B, F)
        y_rhs = min(D, H)
        y_overlap = max(y_rhs - y_lhs, 0)

        rect1 = (C - A) * (D - B)
        rect2 = (G - E) * (H - F)

        return rect1 + rect2 - y_overlap * x_overlap