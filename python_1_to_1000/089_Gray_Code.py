_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/gray-code/
# The gray code is a binary numeral system where two successive values differ in only one bit.
# Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code.
# A gray code sequence must begin with 0. For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
# 00 - 0, 01 - 1, 11 - 3, 10 - 2

# Grey sequence of n + 1 is formed starting with sequence for n, then appending the reverse of that sequence with
# the extra bit set.
# GC(0) = [0], GC(1) = [0,1], GC(2) = [0,1,3,2], GC(3) = [0,1,3,2,6,7,5,4]
# Time - O(2**n)
# Space - O(2**n)

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        gray = [0]

        for i in range(n):
            gray += [x + 2 ** i for x in reversed(gray)]

        return gray

