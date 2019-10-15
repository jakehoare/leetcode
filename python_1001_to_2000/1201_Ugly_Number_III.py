_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/ugly-number-iii/
# Write a program to find the n-th ugly number.
# Ugly numbers are positive integers which are divisible by a or b or c.

# Given a guess for the nth ugly number, we can count the ugly numbers <= guess.
# Count all the numbers divisible by a, b and c. Subtract the numbers divisible by the lowest common multiple of
# each pair from a, b and c. Add back numbers divisible by the lowest common multiple of a, b and c.
# Binary search the range of possible results.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        def gcd(x, y):  # x >= y
            while y != 0:
                x, y = y, x % y
            return x

        def lcm(x, y):
            return (x * y) // gcd(x, y)

        a, b, c = sorted([a, b, c])
        ab, ac, bc = lcm(b, a), lcm(c, a), lcm(c, b)
        abc = lcm(bc, a)

        def ugly_less_or_equal(x):              # count ugly <= x
            result = (x // a) + (x // b) + (x // c)
            result -= (x // ab) + (x // ac) + (x // bc)
            result += x // abc
            return result

        lower, upper = 1, 2 * 10 ** 9

        while lower < upper:
            mid = (lower + upper) // 2
            if ugly_less_or_equal(mid) >= n:    # mid or lower is potentially correct
                upper = mid
            else:                               # result must be above lower
                lower = mid + 1

        return lower
