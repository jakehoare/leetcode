_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/my-calendar-ii/
# Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not
# cause a triple booking.
# Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open
# interval [start, end), the range of real numbers x such that start <= x < end.
# A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common
# to all 3 events.)
# For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully
# without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
# Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

# Create unsorted lists of double bookings and events. For a new booking, return False if overlap with and double
# booking. Else check for overlap with each existing interval and if so, append overlap to doubles.
# List of doubles may contain overlaps but no triple booking is permitted.
# Time - O(n**2)
# Space - O(n)

class MyCalendarTwo(object):

    def __init__(self):
        self.doubles = []       # intervals with double bookings
        self.intervals = []     # all intervals

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i, j in self.doubles:   # check overlap with existing double bookings
            if start < j and end > i:
                return False

        for i, j in self.intervals: # check overlap with existing bookings
            if start < j and end > i:
                self.doubles.append((max(start, i), min(end, j)))

        self.intervals.append((start, end))     # add to list of all events

        return True
