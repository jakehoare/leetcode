_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-covered-intervals/
# Given a list of intervals, remove all intervals that are covered by another interval in the list.
# Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.
# After doing so, return the number of remaining intervals.

# Sort the intervals and iterate over them.
# Maintain a stack of intervals that are not covered.
# For each new interval, if the to of stack interval ends before the interval ends it is not covered.
# Time - O(n log n)
# Space - O(n)

class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        stack = []
        intervals.sort()

        for interval in intervals:
            if not stack or stack[-1][1] < interval[1]:     # keep if not covered
                stack.append(interval)

        return len(stack)
