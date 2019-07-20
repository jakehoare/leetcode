_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/corporate-flight-bookings/
# There are n flights, and they are labeled from 1 to n.
# We have a list of flight bookings.
# A booking [i, j, k] means that we booked k seats from flights labeled i to j inclusive.
# Return an array answer of length n, representing the number of seats booked on each flight in order of their label.

# Create the result with the changes of seats,
# i.e. increment result[start - 1] by seats and decrement result[end] by seats.
# Then update the result by iterating and summing the cumulative changes.
# Time - O(m + n), number of bookings + number of flights
# Space - O(n)

class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        result = [0] * (n + 1)
        for start, end, seats in bookings:
            result[start - 1] += seats
            result[end] -= seats

        seats = 0
        for i, change in enumerate(result):
            seats += change
            result[i] = seats

        return result[:-1]  # remove any change after final flight
