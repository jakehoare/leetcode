_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i],
# obtaining a profit of profit[i].
# You're given the startTime , endTime and profit arrays, you need to output the maximum profit you
# can take such that there are no 2 jobs in the subset with overlapping time range.
# If you choose a job that ends at time X you will be able to start another job that starts at time X.

# Dynamic programming. Build a list of [end_time, max_profit] for the profit that can be made by end_time,
# where profit is strictly ascending.
# Zip the end, start and profits together into tuples and sort by ascending end time.
# For each start time, find the max profit that can be made for all previous jobs finishing at or before that end time.
# If that previous profit + the job profit is more than the best profit, append [end_time, max_profit] to the
# dynamic programming list.
# Time - O(n log n)
# Space - O(n)

import bisect

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        dp = [[0, 0]]  # list of [end_time, max_profit] with ascending max_profit

        jobs = sorted(zip(endTime, startTime, profit))

        for end, start, gain in jobs:
            i = bisect.bisect_right(dp, [start, float("inf")])
            if gain + dp[i - 1][1] > dp[-1][1]:
                dp.append([end, gain + dp[i - 1][1]])

        return dp[-1][1]
