_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/
# Given an array of integers A, find the number of triples of indices (i, j, k) such that:
# 0 <= i < A.length
# 0 <= j < A.length
# 0 <= k < A.length
# A[i] & A[j] & A[k] == 0, where & represents the bitwise-AND operator.

# Count the numbers of ways to form the AND for all pairs.
# For each number, if the AND with any AND of a pair is zero then add the count of all pairs to the result.
# Time - O(n**2) since the number of pairs is limited by the 2**16 for 16 bit elements of A. Calculation of pairs takes
# O(n**2) but the calculation of result takes O(n).
# Space - O(n**2)

from collections import defaultdict

class Solution:
    def countTriplets(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        pairs = defaultdict(int)

        for num1 in A:
            for num2 in A:
                pairs[num1 & num2] += 1

        result = 0
        for pair, count in pairs.items():
            for num3 in A:
                if pair & num3 == 0:
                    result += count
        return result
