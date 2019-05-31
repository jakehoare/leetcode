_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.
# Now given all the cities and fights, together with starting city src and the destination dst, your task is to find
# the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

# Create an adjacency list mapping from a city to all cities connected by a direct flight.
# Create a priority queue ordered by cost. Repeatedly pop city with lowest cost and add it to visited set. If not
# the destination,
# Time - O(m + n log n) where m == len(flights) and n == number of cities
# Space - O(m + n)

from collections import defaultdict
import heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        flts = defaultdict(list)                    # map city to list of (destination, cost)
        for start, end, cost in flights:
            flts[start].append((end, cost))

        queue = [(0, -1, src)]                      # -1 stops since zero stops are direct flights
        visited = set()                             # cities where we know the cheapest cost

        while queue:

            cost, stops, location = heapq.heappop(queue)
            visited.add(location)

            if location == dst:
                return cost

            if stops == K:                          # cannot make more stops along this path
                continue

            for end, next_cost in flts[location]:
                if end not in visited:              # do not revisit cities where we already have the cheapest cost
                    heapq.heappush(queue, (cost + next_cost, stops + 1, end))

        return -1                                   # destination cannot be reached
