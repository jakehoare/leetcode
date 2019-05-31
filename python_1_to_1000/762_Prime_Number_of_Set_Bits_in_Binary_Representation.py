_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
# Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set
# bits in their binary representation.
# The number of set bits an integer has is the number of 1s present when written in binary.

# For each number in the range, convert to binary string, count the number of 1s and check if the count is prime.
# Time - O(n log n) where n == R
# Space - O(log n)

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        result = 0
        primes = {2, 3, 5, 7, 11, 13, 17, 19}

        for i in range(L, R + 1):
            if bin(i).count("1") in primes:
                result += 1

        return result