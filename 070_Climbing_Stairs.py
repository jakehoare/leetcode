_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/climbing-stairs/
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Dynamic programming.  Bases cases of 0 way for n<0 and 1 way for n == 1.  Else nb ways after 1 or 2 steps.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [0] + [-1] * n           # use list instead of dict since known size
        return self.stairs(n, memo)

    def stairs(self, n , memo):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if memo[n] != -1:
            return memo[n]

        result = self.stairs(n-1, memo) + self.stairs(n-2, memo)
        memo[n] = result
        return result
