_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/k-th-smallest-prime-fraction/
# A sorted list A contains 1, plus some number of primes.
# Then, for every p < q in the list, we consider the fraction p/q.
# What is the K-th smallest fraction considered?  Return your answer as an array of ints,
# where answer[0] = p and answer[1] = q.

# Binary search the space of numbers between 0 and 1 for the number with K smaller fractions.
# Since max prime is N = 30000 then min difference between two fractions is 1/N**2 > 10**-9. Hence binary search until
# the solution range < 10**-9.
# For each numerator in turn, test greater denominators to find the first fraction < mid. Next numerator starts with
# previous denominator.
# Time - O(n ln k) where n is number of primes and k is max prime
# Space - O(1)

class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        def count_smaller_fractions(x):     # return number for fractions < x and largest such fraction

            count, denominator, largest = 0, 1, [0, 1]

            for numerator in range(len(A) - 1):     # for each numerator, find first denominator so fraction < x

                while denominator < len(A) and A[numerator] >= x * A[denominator]:  # fraction >= x
                    denominator += 1

                if denominator != len(A) and A[numerator] * largest[1] > largest[0] * A[denominator]:
                    largest = [A[numerator], A[denominator]]                        # new largest

                count += len(A) - denominator       # count this and all greater denominators

            return count, largest

        low, high = 0, 1.0
        while high - low > 10 ** -9:

            mid = (low + high) / 2
            count, largest = count_smaller_fractions(mid)
            if count < K:           # insufficient fractions below mid, search larger candidates
                low = mid
            else:                   # sufficient fractions below mid, search smaller candidates
                result = largest    # update largest fraction where count == K
                high = mid

        return result