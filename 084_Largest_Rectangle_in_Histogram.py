_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/largest-rectangle-in-histogram/
# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.

# For each bar, find the largest rectangle including that bar as the lowest bar.
# An index is popped from the stack when a lower bar to the right is found.
# We calculate the largest area with the bar at the popped index as the height (lowest bar in rectangle).
# Width is determined by loses lower bar to the left and right.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        heights = [0] + heights + [0]   # stack will not be empt and last genuine bar will be popped
        stack = [0]                     # indices of bars in non-decreasing height order

        for i, bar in enumerate(heights[1:], 1):

            while heights[stack[-1]] > bar:     # pop taller off stack

                height = heights[stack.pop()]   # form rectangle with popped bar determining height
                width = i - stack[-1] - 1       # i and stack[-1] - 1 are the first lower bars on left and right
                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area

