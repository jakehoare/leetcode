_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/container-with-most-water/
# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai),
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Start with the widest separation of lines.  To form a greater area, any lesser separation must have a greater
# minimum boundary height.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        max_area = (right - left) * min(height[right], height[left])

        while left < right:
            if height[left] < height[right]:    # By moving in the lower boundary we have the possibility
                left += 1                       # of finding a larger area.
            else:
                right -= 1
            max_area = max(max_area, (right - left) * min(height[right], height[left]))

        return max_area