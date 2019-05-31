_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/perfect-number/
# We define a Perfect Number as a positive integer that is equal to the sum of all its positive divisors except itself.
# Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

# Check all divisor integers up to and including sqrt(num). If divisor has no remainder, add divisor and result of
# division.
# Time - O(n**0.5)
# Space - O(1)

import math

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:                                    # negative, 0 and 1 are not perfect
            return False

        sum_divisors = 1

        for i in range(2, int(math.sqrt(num)) + 1):     # sqrt slightly faster than num**0.5

            div, mod = divmod(num, i)
            if mod == 0:
                sum_divisors += i + div

        return sum_divisors == num