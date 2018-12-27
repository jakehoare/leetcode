_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/array-of-doubled-pairs/
# Given an array of integers A with even length, return true if and only if it is possible to reorder it
# such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.

# Solution requires that numbers are paired as (num, num * 2), hence each element of the input must be the lower
# or higher member of such a pair. Construct pairs from lowest absolute element first.
# Count occurrences of each number. For each unique number starting with the smallest absolute value, if the count of
# num * 2 is less than the count of num then we cannot construct the required list of pairs. Otherwise reduce the
# remaining count of num * 2.
# Time - O(n)
# Space - O(n)

from collections import Counter

class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        counts = Counter(A)

        for num in sorted(counts, key=abs):     # iterate over keys sorted by absolute value

            if counts[num] > counts[num * 2]:
                return False
            counts[num * 2] -= counts[num]

        return True