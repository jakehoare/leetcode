_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/smallest-integer-divisible-by-k/
# Given a positive integer K, you need find the smallest positive integer N such that N is divisible by K,
# and N only contains the digit 1.
# Return the length of N.  If there is no such N, return -1.

# If K is divisible by 2 or 5 then we can never find a multiplier m such that Km has least significant digit of 1.
# Try all possible N in the sequence 1, 11, 111, 1111, ... testing whether there is no remainder from N // K.
# If no remainder, return the length of N. Else retain the remainder and add to set of remainders seen.
# If the same remainder is repeated then there is a cycle and a result cannot be found.
# Time - O(K) since there may be upto K possible reminders
# Space - O(K)

class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        if K % 10 not in {1, 3, 7, 9}:
            return -1

        mod_N, mod_set = 0, set()

        for length in range(1, K + 1):      # iterate the length of N upto K
            mod_N = (10 * mod_N + 1) % K
            if mod_N == 0:
                return length
            if mod_N in mod_set:            # mod_N has been seen before
                return -1
            mod_set.add(mod_N)

        return -1
