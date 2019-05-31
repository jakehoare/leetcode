_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/strobogrammatic-number-ii/
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Find all strobogrammatic numbers that are of length = n.

# Base case of single strobogrammatic digits for odd n, empty string for even n.
# Create numbers of length i by adding pairs of strobogrammatic digits before and after all numbers of length i-2.
# Remove results with leading zero unless single digit.
# Time - O(5**(n//2)), each number of length n-2 is wrapped by 5 pairs to produce numbers of length n
# Space - O(5**(n//2))

import time

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return ['']

        if n % 2 == 1:
            results = ['0', '1', '8']
        else:
            results = ['']

        strobo = {'0' : '0', '1' : '1', '8': '8', '6' : '9', '9' : '6'}
        for i in range(n//2):
            results = [c + r + strobo[c] for r in results for c in strobo]

        return [result for result in results if (result[0] != '0' or n == 1)]
