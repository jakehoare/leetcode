_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-time-difference/
# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any
# two time points in the list.

# Convert times to minutes, append first time + 24hrs so neighboring pairs list all differences are listed and find min
# Time - O(n log n)
# Space - O(n)

class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        minutes = []
        for time in timePoints:
            hrs, mins = time.split(":")
            minutes.append(int(hrs) * 60 + int(mins))

        minutes.sort()
        minutes.append(minutes[0] + 24 * 60)  # len(minutes) guaranteed to be >= 2

        min_diff = 24 * 60
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])

        return min_diff