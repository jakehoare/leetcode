_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/equal-rational-numbers/
# Given two strings S and T, each of which represents a non-negative rational number,
# return True if and only if they represent the same number.
# The strings may use parentheses to denote the repeating part of the rational number.
# In general a rational number can be represented using up to three parts: an integer part, a non-repeating part,
# and a repeating part.
# The number will be represented in one of the following three ways:
# <IntegerPart> (e.g. 0, 12, 123)
# <IntegerPart><.><NonRepeatingPart>  (e.g. 0.5, 1., 2.12, 2.0001)
# <IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)> (e.g. 0.1(6), 0.9(9), 0.00(1212))
# The repeating portion of a decimal expansion is conventionally denoted within a pair of round brackets.  For example:
# 1 / 6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66)
# Both 0.1(6) or 0.1666(6) or 0.166(66) are correct representations of 1 / 6.

# Convert each string to a fraction. As a fraction, the repeating part is divided by nines.
# For example 0.(52) is 52/99 and 0.1(52) is 1/10 + 52/990
# Time - O(n + m), lengths of input strings
# Space - O(n + m)

from fractions import Fraction

class Solution:
    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def to_numeric(s):

            if not ("(") in s:                      # no repeating part
                return Fraction(s)

            non_repeat, repeat = s.split("(")
            repeat = repeat[:-1]                    # remove closing brace

            _, non_repeat_decimal = non_repeat.split(".")

            fract = Fraction(int(repeat), (10 ** len(repeat) - 1) * (10 ** len(non_repeat_decimal)))

            return Fraction(non_repeat) + fract

        return to_numeric(S) == to_numeric(T)
