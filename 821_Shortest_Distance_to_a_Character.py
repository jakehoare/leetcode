_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shortest-distance-to-a-character/
# Given a string S and a character C, return an array of integers representing the shortest distance from the
# character C in the string.
# S string length is in [1, 10000].
# C is a single character, and guaranteed to be in string S.
# All letters in S and C are lowercase.

# Iterate from left to right, for each character recording the distance from the previous C. The iterate from right
# to left, updating the distance from the previous C if lower.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        shortest = []

        prev_C = float("-inf")          # index of previous C
        for i, c in enumerate(S):

            if c == C:
                prev_C = i
            shortest.append(i - prev_C)

        next_C = float("inf")
        for i in range(len(S) - 1, -1, -1):

            c = S[i]
            if c == C:
                next_C = i
            shortest[i] = min(shortest[i], next_C - i)

        return shortest