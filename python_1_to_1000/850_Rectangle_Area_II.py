_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/rectangle-area-ii/
# We are given a list of (axis-aligned) rectangles.  Each rectangle[i] = [x1, y1, x2, y2], where (x1, y1) are the
# coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the ith rectangle.
# Find the total area covered by all rectangles in the plane.
# Since the answer may be too large, return it modulo 10^9 + 7.

# Create a sorted list of opening and closing edges along the x direction. For each edge in the x direction, add the
# area covered in the y direction * the distance since the previous x edge to the area. Update the set of rectangles
# alive at x, then create a sorted list of y direction edges of alive rectangles. Iterate along the y edges, updating
# the y length between y edges provided some rectangle is alive.
# Time - O(n**2 log n)
# Space - O(n)

class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        x_events = []                       # edges of rectangles along x axis (x, start, index)
        for i, (x1, y1, x2, y2) in enumerate(rectangles):
            x_events.append((x1, True, i))
            x_events.append((x2, False, i))
        x_events.sort()

        area = 0
        alive = set()                       # all rectangle indices currently alive at this value of x
        y_coverage = 0                      # the length covered by rectangle in y direction
        x_prev = 0

        for x, start, i in x_events:

            area += (x - x_prev) * y_coverage   # update the area as the distance since previous x * y length covered
            x_prev = x

            if start:                       # update the alive set for this edge
                alive.add(i)
            else:
                alive.discard(i)

            y_events = []                   # edges of alive rectangles along y axis
            for i in alive:
                y_events.append((rectangles[i][1], 1))  # opening edge
                y_events.append((rectangles[i][3], -1)) # closing edge
            y_events.sort()

            y_coverage = 0
            prev_y = 0
            alive_y = 0                     # count of open rectangles
            for y, start_y in y_events:

                if alive_y > 0:             # some rectangle(s) are alive so cover length since previous y
                    y_coverage += y - prev_y

                alive_y += start_y          # increment or decrement the alive count
                prev_y = y

        return area % (10 ** 9 + 7)

