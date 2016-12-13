_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/meeting-rooms-ii/
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
# find the minimum number of conference rooms required.

# Use a heap to store the end times of meetings that have not finished.  For each new meeting in start time order,
# push it onto heap, pop all meetings that have already ended and update max_rooms being used.
# Alternatively, use heap to store the end times of all meetings that need their own rooms.  If a new meeting does
# not overlap with the earliest ending existing meeting then replace existing with new meeting. New meet will overlap
# with all others on heap.
# Time - O(n log n)
# Space - O(n)

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        max_rooms = 0
        rooms = []                              # heap of end times of overlapping meetings
        intervals.sort(key=lambda x: x.start)  # sort by start time

        for interval in intervals:

            heapq.heappush(rooms, interval.end)
            while rooms[0] <= interval.start:   # pop all meetings that have ended before this meeting starts
                heapq.heappop(rooms)
            max_rooms = max(max_rooms, len(rooms))

        return max_rooms


class Solution2(object):
    def minMeetingRooms(self, intervals):
        overlaps = []
        intervals.sort(key=lambda x: x.start)

        for interval in intervals:

            if overlaps and interval.start >= overlaps[0]:  # starts after earliest end time so replace
                heapq.heapreplace(overlaps, interval.end)
            else:                                           # overlaps so push to heap
                heapq.heappush(overlaps, interval.end)

        return len(overlaps)