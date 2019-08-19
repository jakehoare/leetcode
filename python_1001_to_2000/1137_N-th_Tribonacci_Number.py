_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/n-th-tribonacci-number/
# The Tribonacci sequence Tn is defined as follows:
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.

# Repeatedly make the next elements of the sequence from the sum of the last 3 elements.
# Alternatively, use a queue and retain only 3 elements to resuce space to O(1).
# Time - O(n)
# Space - O(n)

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0, 1, 1]
        while len(nums) <= n:
            nums.append(sum(nums[-3:]))

        return nums[n]
