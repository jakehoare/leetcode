_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/circular-permutation-in-binary-representation/
# Given 2 integers n and start. Your task is return any permutation p of (0,1,2.....,2^n -1) such that :
# p[0] = start
# p[i] and p[i+1] differ by only one bit in their binary representation.
# p[0] and p[2^n -1] must also differ by only one bit in their binary representation.

# Find a permutation starting from 0, then move the part from start to the front.
# To find the permutation for n, start with the permutation for n - 1.
# Append to the n - 1 permutation the elements in reverse order with an additional first bit set.
# Time - O(2 ** n)
# Space - O(2 ** n)

class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """
        def helper(i):
            if i == 1:
                return [0, 1]
            temp = helper(i - 1)
            power = 2 ** (i - 1)
            return temp + [power + t for t in temp[::-1]]

        perms = helper(n)
        i = perms.index(start)
        return perms[i:] + perms[:i]
