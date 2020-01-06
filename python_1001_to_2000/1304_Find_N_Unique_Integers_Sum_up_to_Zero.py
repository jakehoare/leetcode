_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# Given an integer n, return any array containing n unique integers such that they add up to 0.

# Use integers 1, 2, ... n // 2 and their negatives.
# If n is odd, also append zero.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ints = [i for i in range(1, (n // 2) + 1)]
        ints += [-i for i in ints]
        return ints if n % 2 == 0 else ints + [0]
