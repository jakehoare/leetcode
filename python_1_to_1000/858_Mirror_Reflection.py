_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/mirror-reflection/
# There is a special square room with mirrors on each of the four walls.
# Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.
# The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a
# distance q from the 0th receptor.
# Return the number of the receptor that the ray meets first.
# It is guaranteed that the ray will meet a receptor eventually.

# Simulate the reflections. After k steps the vertical distance is kq, if this is divisible by p, we are at a corner.
# Identify which corner according to whether the number of reflections is odd or even and whether the vertical distance
# is an odd or even multiple of the side length.
# Time - O(p), all possible points on the wall could be visited before finding a corner
# Space - O(1)

class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        k = 1
        while (k * q) % p != 0:         # vertical distance kq is not a multiple of side length p
            k += 1

        if k % 2 == 0:                  # even number of steps
            return 2
        if ((k * q) // p) % 2 == 0:     # vertical distance kq is an even multiple of side length p
            return 0
        return 1