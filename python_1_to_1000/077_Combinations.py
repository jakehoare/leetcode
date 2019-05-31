_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/combinations/
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# Recursively ignore the last number and choose k form n-1, or use the last number and combine with k-1 from n-1.
# Time - O(k * n! / (k! * (n-k)!)), nCk combinations each of length k
# Space - O(k * n! / (k! * (n-k)!))

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:          # or if k == 1 return [[i] for i in range(1,n+1)]
            return [[]]
        if n < k:           # or if k == n return [[i for i in range(1,n+1)]]
            return []

        without_last = self.combine(n-1, k)

        with_last = [[n] + combo for combo in self.combine(n-1, k-1)]

        return with_last + without_last

