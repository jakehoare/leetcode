_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/count-and-say/
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.

# Iterate through the previous sequence.  When we see a different number, append [1, num] to the new sequence.
# When we see the same number increment its count.
# Time - O(2^n), the sequence at worst doubles each step
# Space - O(2^n)

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        sequence = [1]
        for _ in range(n-1):
            next = []
            for num in sequence:
                if not next or next[-1] != num:
                    next += [1, num]
                else:
                    next[-2] += 1
            sequence = next

        return "".join(map(str, sequence))

