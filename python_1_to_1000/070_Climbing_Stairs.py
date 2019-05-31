_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/climbing-stairs/
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Dynamic programming.  Base cases of no ways for n <= 0, 1 way for n == 1 and 2 ways for n == 2.
# For each additional step, the number of ways is taking one step from the previous step + taking two steps from the
# step before that. Result is a Fibonacci sequence.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n <= 2:
            return n

        stairs, prev = 2, 1         # 2 ways to reach second step, one way to reach first
        for _ in range(3, n + 1):
            stairs, prev = stairs + prev, stairs

        return stairs
