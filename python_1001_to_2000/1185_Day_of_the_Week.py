_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/day-of-the-week/
# Given a date, return the corresponding day of the week for that date.
# The input is given as three integers representing the day, month and year respectively.
# Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday",
# "Thursday", "Friday", "Saturday"}.

# Find the number of days since 1 Jan 1971.
# Sum the day of the month + days in previous months + 365 * years since 1971.
# Add an offset of 4 since 1/1/71 was Friday.
# Add extra days for any previous leap yeas and current leap year.
# Time - O(1)
# Space - O(1)

class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        cumulative_days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

        days = 4 + day + cumulative_days[month - 1] + 365 * (year - 1971)   # 4 for offset from 1/1/1974

        leap_days = (year - 1969) // 4      # number of completed leap years
        print(leap_days)
        if year % 4 == 0 and month >= 3:    # include 29th February in current year
            leap_days += 1
        days += leap_days

        return weekdays[days % 7]
