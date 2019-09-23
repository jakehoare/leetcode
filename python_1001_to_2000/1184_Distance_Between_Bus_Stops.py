_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/distance-between-bus-stops/
# A bus has n stops numbered from 0 to n - 1 that form a circle.
# We know the distance between all pairs of neighboring stops where distance[i] is the distance between the
# stops number i and (i + 1) % n.
# The bus goes along both directions i.e. clockwise and counterclockwise.
# Return the shortest distance between the given start and destination stops.

# Ensure destination stop is not before start stop by swapping if necessary.
# Find the sum of the distances from start to destination.
# Also find the sum of the distances round a complete circuit of all stops.
# Return the minimum of the direct distance and the distance in the reverse direction.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if destination < start:
            start, destination = destination, start

        start_to_dest = sum(distance[start:destination])
        circuit = sum(distance)     # distance of complete circuit
        return min(start_to_dest, circuit - start_to_dest)
