_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/beautiful-array/
# For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:
# For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].
# Given N, return any beautiful array A.  (It is guaranteed that one exists.)

# The condition is equivalent to saying that the average of a pair of numbers cannot be between those numbers.
# Make separate arrays of even and odd numbers, since when concatenated the average of an even and and odd number is
# not an integer so does not violate the required condition.
# Note also that if an array is beautiful a common factor can be added to or multiplied by all elements and it
# remains beautiful. Hence create odds and evens arrays of the required lengths using integers, then scale the
# elements to the required odd or even numbers.
# Time - O(n log n)
# Space - O(n log n)

class Solution:
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        if N == 1:
            return [1]

        evens = self.beautifulArray(N // 2)
        if N % 2 == 0:          # reuse same array if odds and evens are same length
            odds = evens[:]
        else:
            odds = self.beautifulArray((N + 1) // 2)

        odds = [(2 * i) - 1 for i in odds]
        evens = [2 * i for i in evens]

        return evens + odds