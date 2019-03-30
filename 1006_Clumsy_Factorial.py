_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/clumsy-factorial/
# Normally, the factorial of a positive integer n is the product of all positive integers less than or equal to n.
# For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.
# We instead make a clumsy factorial: using the integers in decreasing order, we swap out the multiply operations
# for a fixed rotation of operations: multiply (*), divide (/), add (+) and subtract (-) in this order.
# For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.
# However, these operations are still applied using the usual order of operations of arithmetic: we do all
# multiplication and division steps before any addition or subtraction steps, and multiplication and division steps
# are processed left to right.
# Additionally, the division that we use is floor division such that 10 * 9 / 8 equals 11.
# This guarantees the result is an integer.
# Implement the clumsy function as defined above: given an integer N, it returns the clumsy factorial of N.

# For N from 1 to 4 the results are 1, 2 * 1 = 2, 3 * 2 // 1 = 6 and 4 * 3 // 2 + 1 = 7.
# For larger N (>= 5), N * (N - 1) // (N - 2) = N + 1. Hence we can simplify the series,
# N * (N - 1) // (N - 2) + (N - 3) - (N - 4) * (N - 5) // (N - 6) + (N - 7) - (N - 8) .... =
# (N + 1) + (N - 3) - (N - 4) * (N - 5) // (N - 6) + (N - 7) - (N - 8) * .... =
# (N + 1) + (N - 3) - (N - 3) + (N - 7) - (N - 8) * .... =
# (N + 1) + (N - 3) - (N - 3) + (N - 7) - (N - 7) * .... =
# (N + 1) + ...
# Time - O(1)
# Space - O(1)

class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 2:
            return N
        if N <= 4:
            return N + 3

        if (N - 4) % 4 == 0:    # (N+1) + ... + 5 - (4*3/2) + 1
            return N + 1
        if (N - 4) % 4 <= 2:    # (N+1) + ... + 6 - (5*4/3) + 2 - 1 or (N+1) + ... + 7 - (6*5/4) + 3 - 2 * 1
            return N + 2

        return N - 1            # (N+1) + ... + 8 - (7*6/5) + 4 - 3 * 2 / 1
