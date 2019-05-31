_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/construct-the-rectangle/
# For a web developer, it is very important to know how to design a web page's size.
# So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose
# length L and width W satisfy the following requirements:
# 1. The area of the rectangular web page you designed must equal to the given target area.
# 2. The width W should not be larger than the length L, which means L >= W.
# 3. The difference between length L and width W should be as small as possible.
# You need to output the length L and the width W of the web page you designed in sequence.

# Find the largest integer less than or equal to the square root of the area that divides the area. Try the integer
# less than or equal to the square root and if it does not divide area, decrement until it does.
# Time - O(area**0.5)
# Space - O(1)

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        side = int(area ** 0.5)

        while area % side != 0:         # decrement to find shorter side, faster than increment to find longer side
            side -= 1

        return [area // side, side]
