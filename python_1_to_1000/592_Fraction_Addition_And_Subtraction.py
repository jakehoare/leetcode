_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/fraction-addition-and-subtraction/
# Given a string representing an expression of fraction addition and subtraction, you need to return the calculation
# result in string format. The final result should be irreducible fraction. If your final result is an integer, say 2,
# you need to change it to the format of fraction that has denominator 1. So in this case, 2 should be converted to 2/1.

# Parse the expression into integers, delimited by "/" for numerator and "+" or "-" for denominator. For each fraction,
# find the lowest common multiple of the fraction denominator and the current result denominator. Convert both
# fractions to this denominator and add their numerators to update the result. Repeat for all fractions.
# Divide the result by the lowest common multiple of its numerator and denominator.
# Time - O(n log m) there n is number of fractions and m is hte maximum numerator or denominator
# Space - O(1)

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        def GCD(a, b):  # Euclid's algortihm for greatest common divisor
            div, mod = divmod(a, b)
            if mod == 0:
                return b
            return GCD(b, mod)

        result = [0, 1]  # list of numerator and denominator
        start = 0

        while start < len(expression):
            end = start
            while expression[end + 1] != "/":
                end += 1
            fraction = [int(expression[start:end + 1])]

            start = end = end + 2
            while end + 1 < len(expression) and expression[end + 1] not in ["+", "-"]:
                end += 1
            fraction.append(int(expression[start:end + 1]))

            lcm = fraction[1] * result[1] // GCD(fraction[1], result[1])

            result = [(result[0] * lcm // result[1]) + (fraction[0] * lcm // fraction[1]), lcm]
            start = end + 1

        if result[0] == 0:
            return "0/1"

        gcd = GCD(result[0], result[1])
        return str(result[0] // gcd) + "/" + str(result[1] // gcd)