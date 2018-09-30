_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/nth-magical-number/
# A positive integer is magical if it is divisible by either A or B.
# Return the N-th magical number.  Since the answer may be very large, return it modulo 10^9 + 7.

# Binary search the range of all possible solutions. Given a guess x, the number of magical numbers <= x is
# x // A + x // B - x // lcm(A, B), i.e. all the integers divisible by A + all the integers divisible by B - all the
# integers divisible by both A and B (to avoid double-counting).
# Time - O(1)
# Space - O(1)

class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        low, high = 1, 10 ** 14

        def gcd(a, b):
            a, b = b, a % b
            if b == 0:
                return a
            return gcd(a, b)

        lcm = A * B // gcd(A, B)

        while low < high:

            mid = (low + high) // 2
            num = (mid // A) + (mid // B) - (mid // lcm)    # guess the result
            if num < N:                                     # result must be greater than low
                low = mid + 1
            elif num >= N:                                  # result is at most high
                high = mid

        return low % (10 ** 9 + 7)