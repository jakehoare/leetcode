_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-number-of-refueling-stops/
# A car travels from a starting position to a destination which is target miles east of the starting position.
# Along the way, there are gas stations.
# Each station[i] represents a gas station that is station[i][0] miles east of the starting position,
# and has station[i][1] liters of gas.
# The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.
# It uses 1 liter of gas per 1 mile that it drives.
# When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.
# What is the least number of refueling stops the car must make in order to reach its destination?
# If it cannot reach the destination, return -1.
# Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.
# If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

# Maintain a heap of fuel at previous stations that has not been used. At each station the total fuel used must not be
# less than the distance. If it is less, use fuel from previous stations starting with the largest amounts. If no more
# fuel is unused, we cannot reach the target.
# Time - O(n log n)
# Space - O(n)

import heapq

class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        stops = 0
        fuel = startFuel                                # total fuel used
        past_fuels = []                                 # heap of unused fuel from previous stations
        stations.append([target, 0])                    # target is beyond final station

        for distance, station_fuel in stations:

            while fuel < distance:                      # cannot reach this station without more fuel

                if not past_fuels:                      # no more unused previous stations
                    return -1

                fuel -= heapq.heappop(past_fuels)       # use the previous station with the most fuel
                stops += 1

            heapq.heappush(past_fuels, -station_fuel)   # add this station's fuel to unused fuel

        return stops