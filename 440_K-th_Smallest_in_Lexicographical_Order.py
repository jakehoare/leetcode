_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/
# Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

# Search integers beginning with 1, if not found increment first digit to 2, 3, ... etc.
# Given a beginning digit kth, repeatedly multiply the start and end of search range by 10 until the range includes n.
# If range does not include solution, increment beginning digit kth. Else use kth and multiply range start by 10.

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
                k -= 1     # use kth
                kth *= 10  # next range start

        return kth