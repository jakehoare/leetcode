_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/best-sightseeing-pair/
# Given an array A of positive integers, A[i] represents the value of the i-th sightseeing spot, and two sightseeing
# spots i and j have distance j - i between them.
# The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the sum of the values of the sightseeing
# spots, minus the distance between them.
# Return the maximum score of a pair of sightseeing spots.

# Iterate along the array, tracking the best previous (value - distance).
# For each element, update the result with the element value + best_minus_dist if it is greater than the current
# result. Also update best_minus_dist if it increases and decrement due to the increased distance.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        best_minus_dist = 0
        result = 0

        for num in A:
            result = max(result, num + best_minus_dist)
            best_minus_dist = max(best_minus_dist - 1, num - 1)

        return result
