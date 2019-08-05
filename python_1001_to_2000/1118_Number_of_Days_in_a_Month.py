_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-days-in-a-month/
# Given a year Y and a month M, return how many days there are in that month.

# If February, leap years are divisible by 4 except if divisible by 100 but not 400.
# Else if not February, return 30 or 31 depending on the month.
# Time - O(1)
# Space - O(1)

class Solution(object):
    def numberOfDays(self, Y, M):
        """
        :type Y: int
        :type M: int
        :rtype: int
        """
        if M == 2:                  # February
            if Y % 4 != 0:          # not a leap year if not divisible by 4
                return 28
            if Y % 400 == 0:        # leap year if divisible by 400
                return 29
            if Y % 100 == 0:        # not a leap year if not divisible by 100 but not 400, e.g. 1900
                return 28
            return 29

        if M in [4, 6, 9, 11]:      # not February
            return 30
        return 31
