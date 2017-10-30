_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reconstruct-itinerary/
# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the
# itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when
# read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary.

# Sort the tickets so that for for each starting location the destinations are in reverse alphabetical order.  Create
# a mapping from each start airport to a list of end airports in reverse alphabetical order.  DFS the graph, always
# taking the lexicographically first next airport.  When we reach an end, this airport has an odd number of edges
# and must be the ultimate end of the itinerary so add it to the result.  Backtrack, adding airports to the result
# when there is no other choice, or else exploring.
# Alternatively, iteratively.
# Time - O(n), number of tickets
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        tickets.sort(reverse = True)    # reverse start destination, then ties broken by reverse end
        flights = defaultdict(list)
        for start, end in tickets:      # key is start, value is list of ends (lowest alphabetical is last)
            flights[start].append(end)
        journey = []

        def visit(airport):
            while flights[airport]:
                visit(flights[airport].pop())
            journey.append(airport)

        visit("JFK")
        return journey[::-1]


class Solution2(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        flights = defaultdict(list)
        tickets.sort(reverse = True)

        for start, end in tickets:
            flights[start].append(end)

        route, stack = [], ['JFK']

        while stack:
            while flights[stack[-1]]:                   # while some flight out of top of stack airport
                stack.append(flights[stack[-1]].pop())  # add first flight out to stack
            route.append(stack.pop())                   # no flights out of top of stack - add to result

        return route[::-1]

