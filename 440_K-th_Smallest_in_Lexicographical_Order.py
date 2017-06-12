_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/
# Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

# Search range from and including lower to and excluding upper. Increase range by adding zeros while some part of range
# is less than or equal to n. Then if range does not contain kth, skip past all count numbers and increment range start.
# Else use kth number only and fix first digit.

# Time - O(logn ** 2)
# Space - O(1)

class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        kth = 1
        k -= 1

        while k > 0:

            lower, upper = kth, kth + 1  # check range including lower, excluding upper
            count = 0

            while lower <= n:  # at least some of range is valid
                count += min(upper, n + 1) - lower
                lower *= 10
                upper *= 10

            if count <= k:  # count numbers do not reach k
                k -= count  # use all count numbers
                kth += 1  # increment start point for next range
            else:
                k -= 1  # use kth
                kth *= 10  # next range start

        return kth