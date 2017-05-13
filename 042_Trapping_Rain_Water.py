_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/trapping-rain-water/
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.

# Calculate the highest elevation to the right and to the left of every bar.  Min of these is the max depth of water.
# Subtract the bar height from the max possible depth and floor at zero.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def trap(self, height):

        highest_right = [0] * len(height)
        for i in range(len(height)-2, -1, -1):
            highest_right[i] = max(highest_right[i+1], height[i+1])

        highest_left, depth = [0] * len(height), 0
        for i in range(1, len(height)):     # depth[0] will be 0 so ok for range to start at 1
            highest_left[i] = max(highest_left[i-1], height[i-1])
            depth += max(0, min(highest_left[i], highest_right[i]) - height[i])

        return depth



