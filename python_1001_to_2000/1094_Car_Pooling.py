_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/car-pooling/
# You are driving a vehicle that has capacity empty seats initially available for passengers.
# The vehicle only drives east (ie. it cannot turn around and drive west.)
# Given a list of trips, trip[i] = [num_passengers, start_location, end_location]
# contains information about the i-th trip: the number of passengers that must be picked up,
# and the locations to pick them up and drop them off.
# The locations are given as the number of kilometers due east from your vehicle's initial location.
# Return true if and only if it is possible to pick up and drop off all passengers for all the given trips.

# Sort by ascending start location.
# Iterate over trips, removing from heap all passengers dropped off before the current start location.
# Reduce capacity by the picked up passengers and check if car is too full.
# Else add the end location and number of passengers to the dropoff heap.
# Time - O(n log n)
# Space - O(n)

import heapq

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        trips.sort(key=lambda x: x[1])
        dropoff = []    # heap of (location, nb passengers)

        for pickup, start, end in trips:
            while dropoff and dropoff[0][0] <= start:
                _, dropped = heapq.heappop(dropoff)
                capacity += dropped

            capacity -= pickup
            if capacity < 0:
                return False
            heapq.heappush(dropoff, (end, pickup))

        return True
