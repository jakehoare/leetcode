_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/add-digits/
# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

# Repeatedly sum digitss until < 10.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            num = sum([int(c) for c in str(num)])
        return num