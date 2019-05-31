_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-the-derangement-of-an-array/
# In combinatorial mathematics, a derangement is a permutation of the elements of a set, such that no element appears
# in its original position.
# There's originally an array consisting of n integers from 1 to n in ascending order, you need to find the number
# of derangement it can generate.
# Also, since the answer may be very large, you should return the output mod 1^9 + 7.

# Dynamic programming. Derangements of n numbers can be constructed by,
# 1) putting n at any of the n - 1 locations in a derangement of n - 1 numbers, and moving the number that was at i
#    to the end (location n) +
# 2) taking any arrangement of n - 1 number with one number in the correct place, replacing that correct number with n
#    and moving n to the end.
# Arrangements with one correct are created by putting any number in its correct place and deranging the remainder.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        MODULO = 10 ** 9 + 7
        derange, one_correct = 0, 1

        for i in range(2, n + 1):
            derange, one_correct = (derange * (i - 1) + one_correct) % MODULO, (i * derange) % MODULO

        return derange
