_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/
# Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which randomly and uniformly
# picks an integer point in the space covered by the rectangles.
# An integer point is a point that has integer coordinates.
# A point on the perimeter of a rectangle is included in the space covered by the rectangles.
# ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner,
# and [x2, y2] are the integer coordinates of the top-right corner.

# Create a list of the cumulative areas of the rectangles. Choose random n in [1, total area] and find the
# corresponding rectangle by binary search of the cumulative list. Subtract the areas of all previous rectangles
# to get a point in the rectangle, which is converteed to an x, y coordinate by divide and modulo.
# Time - O(n) for __init__, O(log n) for pick
# Space - O(n)

import bisect, random

class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.cumul_area = [0]       # cumul_area[i] == sum of areas of rects[:i]
        self.x_dimensions = [0]     # x_dimensions[i] == rects[i - 1][2] - rects[i - 1][0]
        self.rects = rects

        for x1, y1, x2, y2 in rects:
            x_dim, y_dim = x2 - x1 + 1, y2 - y1 + 1
            self.x_dimensions.append(x_dim)
            self.cumul_area.append(self.cumul_area[-1] + x_dim * y_dim)

    def pick(self):
        """
        :rtype: List[int]
        """
        n = random.randint(1, self.cumul_area[-1])      # random n in [1, total area]
        i = bisect.bisect_left(self.cumul_area, n)      # index of chosen rectangle
        n -= (self.cumul_area[i - 1] + 1)               # point in rectangle

        dy, dx = divmod(n, self.x_dimensions[i])        # convert n to dx, dy
        x, y = self.rects[i - 1][:2]
        return [x + dx, y + dy]