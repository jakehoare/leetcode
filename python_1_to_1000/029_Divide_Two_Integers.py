_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/divide-two-integers/
# Divide two integers without using multiplication, division and mod operator.
# If overflow, return MAX_INT.

# Repeatedly double the divisor until it would exceed the dividend.  Then repeatedly halve the divisor, subtracting
# it from the dividend whenever possible.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return None
        diff_sign = (divisor < 0) ^ (dividend < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        max_divisor = divisor
        shift_count = 1

        while dividend >= (max_divisor << 1):   # find divisor * 2^i where divisor * 2^(i+1) > dividend
            max_divisor <<= 1
            shift_count <<= 1

        while shift_count >= 1:
            if dividend >= max_divisor:         # subtract max_divisor whenever possible
                dividend -= max_divisor
                result += shift_count
            shift_count >>= 1
            max_divisor >>= 1

        if diff_sign:
            result = -result
        return max(min(result, 2**31-1), -2**31)        # required for leetcode
