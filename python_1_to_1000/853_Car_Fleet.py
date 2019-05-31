_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/car-fleet/
# N cars are going to the same destination along a one lane road.  The destination is target miles away.
# Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the
# target along the road.
# A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.
# The distance between these two cars is ignored - they are assumed to have the same position.
# A car fleet is some non-empty set of cars driving at the same position and same speed.
# Note that a single car is also a car fleet.
# If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.
# How many car fleets will arrive at the destination?

# Sort the cars in decreasing order of position. Iterate over the cars. If a car arrives after the previous car it
# forms a new fleet.
# Time - O(n log n)
# Space - O(n)

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        fleets = 0
        previous = -1                       # time of arrival of previous car at target

        cars = zip(position, speed)
        cars.sort(reverse = True)           # greatest distance first

        for pos, spd in cars:

            time = (target - pos) / float(spd)  # time of arrival at target
            if time > previous:
                fleets += 1
                previous = time                 # new later time of arrival

        return fleets