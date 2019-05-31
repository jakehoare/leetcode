_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/daily-temperatures/
# Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you
# would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
# For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be
# [1, 1, 4, 2, 1, 1, 0, 0]

# Stack contains previous temperatures that do not have a higher temperature, hence is descending. Iterate over
# temperatures, popping off all lower temperatures and updating their results. Then add new temperature and its
# index to stack.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0 for _ in range(len(temperatures))]

        stack = []

        for i, temp in enumerate(temperatures):

            while stack and stack[-1][0] < temp:    # pop and set result for all lower previous temperatures
                _, prev_i = stack.pop()
                result[prev_i] = i - prev_i

            stack.append((temp, i))

        return result