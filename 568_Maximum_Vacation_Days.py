_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-vacation-days/
# LeetCode wants to give one of its best employees the option to travel among N cities to collect algorithm problems.
# But all work and no play makes Jack a dull boy, you could take vacations in some particular cities and weeks. Your
# job is to schedule the traveling to maximize the number of vacation days you could take, but there are certain
# rules and restrictions you need to follow.

# Rules and restrictions:
# You can only travel among N cities, represented by indexes from 0 to N-1. Initially, you are in the city
# indexed 0 on Monday.
# The cities are connected by flights. The flights are represented as a N*N matrix (not necessary symmetrical), called
# flights representing the airline status from the city i to the city j. If there is no flight from the city i to the
# city j, flights[i][j] = 0; Otherwise, flights[i][j] = 1. Also, flights[i][i] = 0 for all i.
# You totally have K weeks (each week has 7 days) to travel. You can only take flights at most once per day and can
# only take flights on each week's Monday morning. Since flight time is so short, we don't consider the impact of
# flight time.
# For each city, you can only have restricted vacation days in different weeks, given an N*K matrix called days
# representing this relationship. For the value of days[i][j], it represents the maximum days you could take vacation
# in the city i in the week j.
# You're given the flights matrix and days matrix, and you need to output the maximum vacation days you could take
# during K weeks.

# Dynamic programming. List stores max vacation days per city starting with the previous week, initally all zero.
# For each week starting from the last and working forward, calculate the max vacation for each city as a) vacation
# from staying in that city and b) for each city with flight, vacation from flying to that city
# Time - O(n**2 * w) cities * weeks
# Space - O(n) number of cities

class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        cities = len(flights)
        weeks = len(days[0])
        if not cities or not weeks:
            return 0

        prev_week_max_days = [0 for _ in range(cities)]

        for week in range(weeks - 1, -1, -1):
            this_week_max_days = [0 for _ in range(cities)]

            for start in range(cities):
                max_vacation = days[start][week] + prev_week_max_days[start]  # stay in same city

                for end in range(cities):
                    if flights[start][end]:  # try all cities with flights
                        max_vacation = max(max_vacation, days[end][week] + prev_week_max_days[end])

                this_week_max_days[start] = max_vacation
            prev_week_max_days = this_week_max_days

        return this_week_max_days[0]