_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/super-ugly-number/
# Write a program to find the nth super ugly number.  Super ugly numbers are positive numbers whose all prime factors
# are in a given list of primes.
# 1 is a super ugly number for any given primes.
# The given numbers in primes are in ascending order.

# Each super ugly number is the product of a prime and a previous super ugly number.  Track the last super ugly number
# to have been multiplied by each prime to create a list of candidates.  Take the smallest candidate(s) from the list
# and replace with it/their next in sequence.
# Alternatively, use a heap to find min(candidates) in log k time if len(primes) is large.
# Time - O(n * k) where k is the length of primes list.
# Space - O(n)

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        super_ugly = [1]
        # super_ugly[indices[i]] is the last super_ugly number to be multiplied by primes[i] to generate candidates[i]
        indices = [0 for _ in range(len(primes))]
        candidates = primes[:]

        while len(super_ugly) < n:

            ugly = min(candidates)
            super_ugly.append(ugly)

            for i in range(len(candidates)):    # update all candidates equal to ugly (avoids duplicates)
                if ugly == candidates[i]:
                    indices[i] += 1
                    candidates[i] = primes[i] * super_ugly[indices[i]]

        return super_ugly[-1]