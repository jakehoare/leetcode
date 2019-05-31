_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/line-reflection/
# Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

# Find the set of the x-values of all points with the same y-value.  For each y-value make a sorted list of distinct
# x-values.  Reflection axis is the mid-point between outer elements of the list.  Only if all other pairs (moving
# from outside of list inwards) match same reflection axis then all points can be reflected.
# Time - O(n log n) due to sorting of x-values
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        y_to_x = defaultdict(set)   # set since multiple points can map to same point
        for x, y in points:
            y_to_x[y].add(x)

        reflection = None           # x-value of reflection line
        for y in y_to_x:
            xs = sorted(list(y_to_x[y]))
            left, right = 0, len(xs) - 1

            if reflection is None:
                reflection = xs[left] + xs[right]   # store sum (= 2 * x-axis of reflection) to maintain integer
                left += 1
                right -= 1

            while left <= right:
                if xs[right] + xs[left] != reflection :
                    return False
                left += 1
                right -= 1

        return True
