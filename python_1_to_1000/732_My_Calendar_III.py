_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/my-calendar-iii/
# Implement a MyCalendarThree class to store your events. A new event can always be added.
# Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open
# interval [start, end), the range of real numbers x such that start <= x < end.
# A K-booking happens when K events have some non-empty intersection (ie., there is some time that is common to all
# K events.)
# For each call to the method MyCalendar.book, return an integer K representing the largest integer such that there
# exists a K-booking in the calendar.
# Your class will be called like this: MyCalendarThree cal = new MyCalendarThree(); MyCalendarThree.book(start, end)

# Maintain a sorted list bookings of x values where the number of events changes. Each entry [x, n] represents n
# overlapping events from point x until the next element of the bookings list.
# Time - O(n**2)
# Space - O(n)

import bisect

class MyCalendarThree(object):

    def __init__(self):
        self.bookings = [[float("-inf"), 0], [float("inf"), 0]]     # sorted list of [x, nb overlaps]
        self.max_booking = 0                                        # maximum number of overlaps

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        i = bisect.bisect_left(self.bookings, [start, -1])          # find insertion index of start

        if self.bookings[i][0] != start:                            # insert if start is new x value
            count = self.bookings[i - 1][1]
            self.bookings.insert(i, [start, count + 1])
            self.max_booking = max(self.max_booking, count + 1)
            i += 1

        while end > self.bookings[i][0]:                            # increment all intervals before end
            self.bookings[i][1] += 1
            self.max_booking = max(self.max_booking, self.bookings[i][1])
            i += 1

        if self.bookings[i][0] != end:                              # insert if end is new x value
            count = self.bookings[i - 1][1]
            self.bookings.insert(i, [end, count - 1])

        return self.max_booking


