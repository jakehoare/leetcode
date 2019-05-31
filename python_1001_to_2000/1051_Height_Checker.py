_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/height-checker/
# Students are asked to stand in non-decreasing order of heights for an annual photo.
# Return the minimum number of students not standing in the right positions.
# This is the number of students that must move in order for all students to be standing in non-decreasing
# order of height.

# Compare the sorted ordering with the original ordering.
# Time - O(n log n)
# Space - O(n)

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))
