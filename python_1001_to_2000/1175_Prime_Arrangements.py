_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/prime-arrangements/
# Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)
# Recall that an integer is prime if and only if it is greater than 1,
# and cannot be written as a product of two positive integers both smaller than it.
# Since the answer may be large, return the answer modulo 10^9 + 7.

# Binary search the list of prines to find how many primes are <= n.
# Multiply the number of permutations of primes (primes!) by the number of permutations of non-primes.
# Time - O(1)
# Space - O(1)

import bisect, math

class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        prime_count = bisect.bisect_right(primes, n)
        return (math.factorial(prime_count) * math.factorial(n - prime_count)) %  (10 ** 9 + 7)
