_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/employee-free-time/
# We are given a list schedule of employees, which represents the working time for each employee.
# Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.
# Return the list of finite intervals representing common, positive-length free time for all employees,
# also in sorted order.

# Maintain a heap of the next meeting start time for every employee. Pop the next meeting start time off the heap and
# replace it with the next interval from that employee (if not the last interval). If start time is after last end time,
# there is free time so add interval to result. Update the last end time to end of this meeting if later than current
# last end time.
# Time - O(m log n) where n is the number of employees and m is the number of meetings.
# Space - O(n)

import heapq

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        employees = len(schedule)
        next_start_times = [(schedule[i][0].start, 0, i) for i in range(employees)]
        heapq.heapify(next_start_times)             # heap of (start time, interval index, employee)
        last_end_time = next_start_times[0][0]      # time when last meeting ended
        result = []

        while next_start_times:

            interval_start_time, interval, employee = heapq.heappop(next_start_times)
            if interval + 1 < len(schedule[employee]):  # add next interval for this employee to heap
                heapq.heappush(next_start_times, (schedule[employee][interval + 1].start, interval + 1, employee))

            if interval_start_time > last_end_time:     # free time between next start time and last end time
                result.append(Interval(last_end_time, interval_start_time))
            last_end_time = max(last_end_time, schedule[employee][interval].end)    # update last end time

        return result
