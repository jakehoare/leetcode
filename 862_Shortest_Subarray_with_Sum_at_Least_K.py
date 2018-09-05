_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
# Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.
# If there is no non-empty subarray with sum at least K, return -1.

# Calculate the prefix sums of the array. Maintain an queue of prefix sums that have not been used in order of
# increasing index.
# For each new prefix sum, update the result using the smallest indices in the queue, as long as the subarray
# sum is >= K. The last value used creates the shortest subarray, so all earlier values can be discarded. The last
# value can be also discarded because all later prefix sums will make longer subarrays.
# Remove from the right of the queue all greater prefixes, since they would make longer subarrays.
# Time - O(n)
# Space - O(n)

from collections import deque

class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)

        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + A[i]

        queue = deque()
        result = n + 1

        for i in range(n + 1):

            while queue and prefix_sums[i] - prefix_sums[queue[0]] >= K:
                result = min(result, i - queue.popleft())   # check and discard in order of decreasing subarray length

            while queue and prefix_sums[queue[-1]] >= prefix_sums[i]:
                queue.pop()                         # remove all greater prefix sums

            queue.append(i)                         # append to right of queue

        return result if result <= n else -1