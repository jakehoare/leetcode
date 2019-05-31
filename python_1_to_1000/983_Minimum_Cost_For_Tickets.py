_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-cost-for-tickets/
# In a country popular for train travel, you have planned some train travelling one year in advance.
# The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.
# Train tickets are sold in 3 different ways:
# a 1-day pass is sold for costs[0] dollars;
# a 7-day pass is sold for costs[1] dollars;
# a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.
# For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.
# Return the minimum number of dollars you need to travel every day in the given list of days.

# For each travel day, for each pass length, find the next travel day not covered by the pass and add the cost of the
# pass to the cost of covering from the next uncovered day onwards. Take the minimum over the 3 pass lengths.
# Memoize previous results.
# Time - O(n), length of days
# Space - O(n)

from typing import *
from functools import lru_cache

class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':

        PASSES = [1, 7, 30]         # days covered

        @lru_cache(None)
        def get_min_cost(i):        # min cost from days[i] onwards

            if i >= len(days):
                return 0

            min_cost = float("inf")
            j = i
            for length, cost in zip(PASSES, costs):
                while j < len(days) and days[j] < days[i] + length:     # find next uncovered travel day by this pass
                    j += 1
                min_cost = min(min_cost, cost + get_min_cost(j))

            return min_cost

        return get_min_cost(0)
