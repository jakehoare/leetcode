_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-cost-to-merge-stones/
# There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.
# A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the
# total number of stones in these K piles.
# Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.

# Return -1 if repeated merges will not leave one stone.
# For a given subarray, try all possible splits into a prefix and a suffix, which are separately merged.
# The prefix may be a single pile (which ensures that there is some value passed to the min function) or any prefixe of
# a length that can be merged.
# If the subarray is of the correct length to be merged, each pile is counted once.
# Time - O(n**3)
# Space - O(n**2)

import functools

class Solution:
    def mergeStones(self, stones, K):

        n = len(stones)
        if (n - 1) % (K - 1) != 0:  # each merge removes K - 1 and must leave 1 remaining
            return -1

        prefix_sum = [0] * (n + 1)  # prefix_sum allows calculation of the sum of stones in a subarray
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]

        @functools.lru_cache(None)
        def helper(i, j):           # merge stones[i:j + 1]

            if j - i + 1 < K:       # cannot merge length less than K
                return 0

            res = min(helper(i, mid) + helper(mid + 1, j) for mid in range(i, j, K - 1))
            if (j - i) % (K - 1) == 0:
                res += prefix_sum[j + 1] - prefix_sum[i]
            return res

        return helper(0, n - 1)
