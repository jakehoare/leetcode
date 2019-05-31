_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/generate-random-point-in-a-circle/
# Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform
# random point in the circle.
# Note:
# input and output values are in floating-point.
# radius and x-y position of the center of the circle is passed into the class constructor.
# a point on the circumference of the circle is considered to be in the circle.
# randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.

# Rejection sampling from the square containing the circle. Choos a random point inside the square with x and y
# between -1 and 1. This has probability of pi / 4 of being in the circle of radius 1. Else repeat until random point
# is in the circle.
# Alternatively use polar coordinates with a random distance and angle. Square root of distance is required to
# normalise the density of points, or else the probability decreases with radius.
# Time - O(1) expected 4 / pi
# Space - O(1)

import random

class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        x, y = 2 * random.random() - 1, 2 * random.random() - 1     # x and y between -1 and 1
        if x * x + y * y > 1:                                       # outside circle, repeat
            return self.randPoint()
        return [x * self.radius + self.x_center, y * self.radius + self.y_center]   # translate from unit circle

    def randPoint2(self):
        radius = random.random() ** 0.5 * self.radius
        angle = random.random() * 2 * math.pi
        return [radius * math.sin(angle) + self.x_center, radius * math.cos(angle) + self.y_center]