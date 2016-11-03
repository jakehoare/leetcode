_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/largest-rectangle-in-histogram/
# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.

# An index is popped from the stack when a lower height is found.  We calculate the largest area with the popped
# index.  Popped index is the lowest height, width is deteremined by i and the next index below on the stack.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        heights.append(0)   # added so last genuine index len(heights)-1 will be popped
        stack = [0]         # indices in increasing height order

        for i in range(1, len(heights)):

            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area



