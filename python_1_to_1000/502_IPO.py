_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/ipo/
# Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode
# would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can
# only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total
# capital after finishing at most k distinct projects.
# You are given several projects. For each project i, it has a pure profit Pi and a minimum capital of Ci is needed to
# start the corresponding project. Initially, you have W capital. When you finish a project, you will obtain its pure
# profit and the profit will be added to your total capital.
# To sum up, pick a list of at most k distinct projects from given projects to maximize your final capital, and output
# your final maximized capital.

# Sort projects in increasing order of capital required. Add all projects available with current capital to heap. Pop
# from heap project with most profit.
# Time - O(n log n)
# Space - O(n)

import heapq

class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        projects = sorted(zip(Capital, Profits))

        i = 0
        available = []  # profits of projects requiring at most current capital W

        while k > 0:

            while i < len(projects) and projects[i][0] <= W:
                heapq.heappush(available, -projects[i][1])
                i += 1

            if not available:   # cannot do any projects
                return W
            best_profit = heapq.heappop(available)

            W -= best_profit
            k -= 1

        return W