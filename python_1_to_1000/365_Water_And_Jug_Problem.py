_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/water-and-jug-problem/
# You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available.
# You need to determine whether it is possible to measure exactly z litres using these two jugs.
# If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.
# Operations allowed:
#   Fill any of the jugs completely with water.
#   Empty any of the jugs.
#   Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.

# z must be a multiple of the greatest common divisor of x and y, and not more than the sum of x and y
# Time - O(log n)
# Space - O(1)


class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        if z == 0:
            return True
        g = gcd(x, y)
        if g == 0:
            return False
        return z % g == 0 and z <= x + y