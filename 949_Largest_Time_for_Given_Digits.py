_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/largest-time-for-given-digits/
# Given an array of 4 digits, return the largest 24 hour time that can be made.
# The smallest 24 hour time is 00:00, and the largest is 23:59.
# Starting from 00:00, a time is larger if more time has elapsed since midnight.
# Return the answer as a string of length 5. If no valid time can be made, return an empty string.

# Check all permutations of the digits. Reject those which are not valid times.
# Time - O(1) since 4! times are possible
# Space - O(1)

from itertools import permutations

class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        best_minutes = -1       # most minutes past midnight

        for time in permutations(A):

            hours = time[0] * 10 + time[1]
            if hours >= 24:
                continue

            minutes = time[2] * 10 + time[3]
            if minutes >= 60:
                continue

            total_minutes = hours * 60 + minutes
            if total_minutes > best_minutes:
                best_minutes = total_minutes
                best = time

        if best_minutes == -1:
            return ""

        best = [str(x) for x in best]
        return "".join(best[:2]) + ":" + "".join(best[2:])