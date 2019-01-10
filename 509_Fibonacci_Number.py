_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/fibonacci-number/
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number
# is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
# Given N, calculate F(N).

# Iterate N times, storing anf updating the last 2 numbers of the sequence.
# Time - O(n)
# Space - O(1)

class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        i, j = 0, 1
        for _ in range(N):
            i, j = j, i + j

        return i
