_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/subarray-sums-divisible-by-k/
# Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

# A sum divisible by K means sum of zero modulo K.
# Dictionary counts the number of prefix sums modulo K. For each element, update the running sum and add to the result
# the count of prefix sums equal to the running sum (subtracting the prefix from the running sum makes a subarray of
# sum 0 modulo K). Then update the dictionary.
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class Solution:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        result = 0
        running_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1

        for num in A:
            running_sum = (running_sum + num) % K
            result += prefix_sums[running_sum]
            prefix_sums[running_sum] += 1

        return result