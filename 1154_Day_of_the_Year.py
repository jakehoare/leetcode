_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/day-of-the-year/
# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD,
# return the day number of the year.

# Find the number of day in the whole months completed, assuming not a leap year.
# Add 29th February if in March or later and a leap year.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        cumulative_days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

        year, month, day = [int(x) for x in date.split("-")]
        result = cumulative_days[month - 1] + day

        if month >= 3 and year % 4 == 0 and year != 1900:   # 1900 was not a leap year
            result += 1
        return result
