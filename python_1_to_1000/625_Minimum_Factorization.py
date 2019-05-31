_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-factorization/
# Given a positive integer a, find the smallest positive integer b whose multiplication of each digit equals to a.
# If there is no answer or the answer is not fit in 32-bit signed integer, then return 0.

# Iterating over the digits from 9 down to 2, find all the factors of each digit. Add each factor to the result from
# the least significant digit first (which minimises the value since we start by removing factors of 9). By starting
# with 9 we minimise the number of factors.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a == 1:
            return 1

        result = 0
        tens = 1

        for digit in range(9, 1, -1):

            while a != 1 and a % digit == 0:

                result += digit * tens

                if result > 2 ** 31:
                    return 0

                a //= digit
                if a == 1:
                    return result
                tens *= 10

        return 0