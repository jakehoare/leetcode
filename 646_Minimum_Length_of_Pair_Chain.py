_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-length-of-pair-chain/
# You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.
# Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in
# this fashion.
# Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs.
# You can select pairs in any order.

# Sort by ascending first number. For each pair, if no overlap with previous end then increment chain and update end
# with pair end. Else replace end with pair end if lower.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: x[0])
        chain = 0
        end = pairs[0][0] - 1

        for pair in pairs:
            if end < pair[0]:
                chain += 1
                end = pair[1]
            else:
                end = min(end, pair[1])

        return chain