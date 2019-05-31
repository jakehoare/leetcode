_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/perfect-rectangle/
# Given N axis-aligned rectangles where N > 0, determine if they together form an exact cover of a rectangular region.
# Each rectangle is represented as a bottom-left point and a top-right point.

# Total area of all rectangles must equal covered region area.  Corners of region must be counted once, other corners
# match either 2 or 4 rectangles.
# Time - O(n), number of rectangles
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        min_r, min_c = float("inf"), float("inf")       # find extent of all rectangles
        max_r, max_c = float("-inf"), float("-inf")
        area = 0                                        # sum of areas of all rectangles
        corners = defaultdict(int)                      # count of number of corner by (r, c)

        for r1, c1, r2, c2 in rectangles:
            area += (r2 - r1) * (c2 - c1)
            min_r = min(min_r, r1)
            min_c = min(min_c, c1)
            max_r = max(max_r, r2)
            max_c = max(max_c, c2)

            corners[(r1, c1)] += 1
            corners[(r2, c2)] += 1
            corners[(r1, c2)] += 1
            corners[(r2, c1)] += 1

        rows = max_r - min_r
        cols = max_c - min_c
        if area != rows * cols:
            return False

        for r, c in corners:
            if r in {min_r, max_r} and c in {min_c, max_c}:
                if corners[(r, c)] != 1:
                    return False
            elif corners[(r, c)] % 2 != 0:
                return False

        return True