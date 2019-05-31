_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/fraction-to-recurring-decimal/
# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.

# Find the initial integer part then repeatedly multiply by 10, divide by denominator and calculate remainder.  If
# same remainder repeats there is a cycle.

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0:
            return None
        decimal = []                        # store result as a list
        if numerator * denominator < 0:     # negative sign
            decimal.append('-')

        output, remainder = divmod(abs(numerator), abs(denominator))    # divide and modulo combined
        decimal.append(str(output))
        if remainder == 0:
            return "".join(decimal)

        decimal.append('.')
        seen = {}                           # key is remainder, value is index in decimal

        while remainder != 0:
            if remainder in seen:
                return "".join(decimal[:seen[remainder]] + ['('] + decimal[seen[remainder]:] + [')'])
            seen[remainder] = len(decimal)
            output, remainder = divmod(remainder*10, abs(denominator))
            decimal.append(str(output))

        return "".join(decimal)

