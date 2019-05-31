_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/bus-routes/
# We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever.
# For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the
# sequence 1->5->7->1->5->7->1->... forever.
# We start at bus stop S (initially not on a bus), and we want to go to bus stop T.
# Travelling by buses only, what is the least number of buses we must take to reach our destination?
# Return -1 if it is not possible.

# Bidirectional breadth-first search.
# Create mapping from each stop to all routes that the stop is on. Maintain front and back frontiers of stops that
# can be reached. Expand the smaller frontier in each round with all stops that have not been visited and are on the
# same route as a stop in the current frontier. Terminate when frontiers intersect or one is empty.
# Time - O(n), number of stops
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        routes = [set(route) for route in routes]       # convert routes so set for faster merging later
        stop_to_routes = defaultdict(set)               # map each stop to set of routes it is on

        for route, stops in enumerate(routes):
            for stop in stops:
                stop_to_routes[stop].add(route)

        front, back = {S}, {T}                          # frontier sets
        visited = set()                                 # stops that should not be visited again
        buses = 0

        while front and back and not (front & back):    # end if either set is empty or there is intersection

            if len(front) < len(back):                  # swap to expand smaller set
                front, back = back, front

            buses += 1
            new_front = set()
            visited |= front                            # add all frontier to visited

            for stop in front:
                for route in stop_to_routes[stop]:
                    new_front |= routes[route]          # add all stops on the routes that stop is on to new_front

            front = new_front - visited                 # remove all visited

        return buses if front & back else -1
