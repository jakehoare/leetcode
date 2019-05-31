_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/happy-number/
# Write an algorithm to determine if a number is "happy".
# A happy number is a number defined by the following process: Starting with any positive integer,
# replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1
# (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this
# process ends in 1 are happy numbers.

# Fast and slow pointers increment to the next sum of square digits.  If in a cycle pointers will converge at
# a value other than 1, if no cycle pointers will both be 1.
# Alternatively, if n == 4 then we are in a cycle.  See https://en.wikipedia.org/wiki/Happy_number
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True, 1
        slow = sum([int(c)*int(c) for c in str(n)])
        fast = sum([int(c)*int(c) for c in str(slow)])

        while fast != slow:
            slow = sum([int(c)*int(c) for c in str(slow)])
            fast = sum([int(c)*int(c) for c in str(fast)])
            fast = sum([int(c)*int(c) for c in str(fast)])

        return slow == 1

class Solution2(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while True:
            if n == 1:
                return True
            if n == 4:
                return False
            n = sum([int(c)*int(c) for c in str(n)])
