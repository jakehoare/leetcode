_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/perfect-squares/
# Given a positive integer n, find the least number of perfect square numbers (e.g., 1, 4, 9, 16, ...) which sum to n.

# Dynamic programming.  memo[i] is the minimum nb squares that sum to i.  While n is not already in memo, extend memo
# to be 1 + min of all previous memo results that are a perfect square number of indices away.
# Time - O(n**1.5)
# Space - O(n)

class Solution(object):

    memo = [0, 1]   # memo is persistent so that calls to numSquares() build on previous results

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while len(self.memo) <= n:
            self.memo.append(1 + min(self.memo[-i*i] for i in range(1, int(len(self.memo)**0.5)+1)))

        return self.memo[n]

