_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/meeting-rooms/
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
# determine if a person could attend all meetings.

# Siort by increasing start time, then check for any meeting starting before previous meeting finishes.
# Time - O(n log n)
# Space - O(1)

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key=lambda x: x.start)

        for i, interval in enumerate(intervals[1:], 1):     # skip first interval

            if interval.start < intervals[i - 1].end:
                return False

        return True