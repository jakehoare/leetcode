_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/meeting-scheduler/
# Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration,
# return the earliest time slot that works for both of them and is of duration duration.
# If there is no common time slot that satisfies the requirements, return an empty array.
# The format of a time slot is an array of two elements [start, end]
# representing an inclusive time range from start to end.
# It is guaranteed that no two availability slots of the same person intersect with each other.
# That is, for any two time slots [start1, end1] and [start2, end2] of the same person,
# either start1 > end2 or start2 > end1.

# Sort both lists by ascending start time.
# Use pointers i and j to the next slot in each list.
# While neither pointer is at the end, find the overlapping time of the current slots.
# If this is long enough, return the meeting.
# Else move the pointer forward for the slot with the earlier start.
# Time - O(m log m + n log n)
# Space - O(m + n)

class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        i, j = 0, 0
        m, n = len(slots1), len(slots2)
        slots1.sort()
        slots2.sort()

        while i < m and j < n:
            # earliest finish - latest start
            latest_start = max(slots1[i][0], slots2[j][0])
            overlap = min(slots1[i][1], slots2[j][1]) - latest_start
            if overlap >= duration:
                return [latest_start, latest_start + duration]

            if slots1[i][0] <= slots2[j][0]:
                i += 1
            else:
                j += 1

        return []
