_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-1-bits/
# Write a function that takes an unsigned integer and returns the number of ’1' bits (known as the Hamming weight).

# Convert to string and count '1' chars.
# Time - O(log n)
# Space - O(log n)

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum(c == "1" for c in bin(n)[2:])