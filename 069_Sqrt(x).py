_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sqrtx/
# Implement int sqrt(int x).
# Compute and return the square root of x.

# Newton method. Initial guess of x. Iteratively update guess to be average of previous guess and x // guess.
# Since guess is too high, x // guess is too low.
# Terminate when guess^2 <= x.
# Time - O((log x)^3) - log x from nb iterations, log x from multiple and log x from divide
# Space - O(1)

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        guess = x
        while guess * guess > x:
            guess = (guess + x // guess) // 2
        return guess

