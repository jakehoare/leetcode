_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/diet-plan-performance/
# A dieter consumes calories[i] calories on the i-th day.
# Given an integer k, for every consecutive sequence of k days
# (calories[i], calories[i+1], ..., calories[i+k-1] for all 0 <= i <= n-k), they look at T,
# the total calories consumed during that sequence of k days (calories[i] + calories[i+1] + ... + calories[i+k-1]):
# If T < lower, they performed poorly on their diet and lose 1 point;
# If T > upper, they performed well on their diet and gain 1 point;
# Otherwise, they performed normally and there is no change in points.
# Initially, the dieter has zero points.
# Return the total number of points the dieter has after dieting for calories.length days.
# Note that the total points can be negative.

# Sliding window of the calories consumed over k days.
# For each day after the end of a window, update points then update window calories.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        calories.append(0)              # append extra dummy element
        window = sum(calories[:k])
        points = 0

        for i in range(k, len(calories)):
            if window < lower:
                points -= 1
            elif window > upper:
                points += 1
            window += calories[i]
            window -= calories[i - k]

        return points
