_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/my-calendar-i/
# Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a
# double booking.
# Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open
# interval [start, end), the range of real numbers x such that start <= x < end.
# A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to
# both events.)
# For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully
# without causing a double booking. Otherwise, return false and do not add the event to the calendar.
# Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

# Create sorted list of events. Binary search for position to insert new event and do so if no overlap with previous
# or next events.
# Time - O(n**2)
# Space - O(n)

import bisect

class MyCalendar(object):

    def __init__(self):
        self.bookings = [(float("-inf"), float("-inf")), (float("inf"), float("inf"))]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        i = bisect.bisect_left(self.bookings, (start, end))

        if end > self.bookings[i][0]:
            return False
        if start < self.bookings[i - 1][1]:
            return False

        self.bookings.insert(i, (start, end))
        return True