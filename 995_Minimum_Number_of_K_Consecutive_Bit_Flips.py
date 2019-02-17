_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/
# In an array A containing only 0s and 1s, a K-bit flip consists of choosing a (contiguous) subarray of length K and
# simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.
# Return the minimum number of K-bit flips required so that there is no 0 in the array.
# If it is not possible, return -1.

# Add flips to a queue. Iterate over A, first removing from the queue all earlier flips that impact elements before
# A[i]. Check the bit A[i], adding all the flips in the current window to the initial bit. Take modulo 2 to find the
# updated bit. If bit is 0, make a new flip.
# Time - O(n)
# Space - O(K)

from collections import deque

class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        flips = 0
        flip_i = deque()            # sliding window of indices of flips

        for i in range(len(A)):

            while flip_i and flip_i[0] + K <= i:    # remove flips that do not affect A[i]
                flip_i.popleft()

            if (A[i] + len(flip_i)) % 2 == 0:       # A[i] must be flipped
                if i > len(A) - K:
                    return -1                       # cannot flip last K elements
                flips += 1
                flip_i.append(i)

        return flips
