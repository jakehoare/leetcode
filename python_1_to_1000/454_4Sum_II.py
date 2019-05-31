_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/4sum-ii/
# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that
# A[i] + B[j] + C[k] + D[l] is zero. All A, B, C, D have same length.

# Count all sums of pairs in lists A and B. For each pair in C and D, increment total by count of -(c + d) from AB.
# Time - O(n**2)
# Space - O(n**2)

from collections import defaultdict

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB = defaultdict(int)
        count = 0

        for a in A:
            for b in B:
                AB[a + b] += 1

        for c in C:
            for d in D:
                if -(c + d) in AB:
                    count += AB[-(c + d)]

        return count