_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-length-of-pair-chain/
# You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.
# Define a pair (c, d) can follow another pair (a, b) if and only if b < c.
# Chain of pairs can be formed in this fashion.
# Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs.
# You can select pairs in any order.

# Sort by first number of the pair. For each pair, if first number is after previous chain end then this pair can be
# used to extend chain to new pair end. Else last member of chain can be replace with new pair if it reduces chain end.
# Replacement is always possible because new pair must have same or larger first member.
# Time - O(n log n)
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