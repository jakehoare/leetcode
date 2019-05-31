_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/largest-palindrome-product/
# Find the largest palindrome made from the product of two n-digit numbers.
# Since the result could be very large, you should return the largest palindrome mod 1337.

# Build palindromes with 2 * n digits, starting from the largest palindrome and check if they can be factorised.
# Define palindrome as upper * 10**n + lower.
# The two factors are M = 10**n - i and L = 10**n - j where i and j are small.
# Hence palindrome = (10**n - i) * (10**n - j) = 10**n * (10**n - (i + j)) + i * j = upper * 10**n + lower.
# So upper = 10**n - (i + j) and lower = i * j.
# Define a = i + j. This means that a = 10**n - upper.
# Substituting for j = a - i, the equation for lower can be rewritten as lower = a * i - i * i.
# Solving for i, in order for i to be an integer sqrt(a**2 - 4 * lower) must be an integer.
# Time - O(n * 10**n) for the for loop
# Space - O(1)

class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9

        for a in range(1, 9 * 10 ** (n - 1)):

            hi = (10 ** n) - a          # most significant digits of palindrome
            lo = int(str(hi)[::-1])     # least significant digits of palindrome

            if a ** 2 - 4 * lo < 0:
                continue

            if (a ** 2 - 4 * lo) ** .5 == int((a ** 2 - 4 * lo) ** .5):     # sqrt(a**2 - 4*lo) is an integer
                return (lo + 10 ** n * (10 ** n - a)) % 1337
