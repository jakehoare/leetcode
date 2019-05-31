_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/super-pow/
# Your task is to calculate a**b mod 1337 where a is a positive integer and b is an extremely large positive integer
# given in the form of an array.

# Base case is 1 (since a cannot be zero).  For each digit of b starting with first, iteratively raise to the power 10
# and multiply by a**digit, all modulo 1337
# Time - O(log b)
# Space - O(1)

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        result = 1

        for digit in b:         # pow() takes modulo as input
            result = (pow(result, 10, 1337) * pow(a, digit, 1337)) % 1337

        return result