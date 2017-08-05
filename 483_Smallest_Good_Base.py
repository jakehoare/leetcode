_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/smallest-good-base/
# For an integer n, we call k>=2 a good base of n, if all digits of n base k are 1.
# Given a string representing n, you should return the smallest good base of n in string format.

# For base b, n = b**k + b**(k-1) + .. n + 1 for some b and max_power k.
# Try max powers from largest (base 2 = binary representation) down to 2. Since n > base**max_power and
# n < (base+1)**max_power, base must be int(n**(1/max_power). Test if true. Fallback to base n-1.
# Time - O(log n)
# Space - O(1)

import math

class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)

        for max_power in range(int(math.log(n, 2)), 1, -1):     # largest max_power implies smallest base

            base = int(n ** max_power ** -1)                    # find the only possible base for this max_power
            if n == ((base ** (max_power + 1)) - 1) // (base - 1):      # sum of geometric series
                return str(base)

        return str(n - 1)   # fallback to base n-1, represents any n as "11"
