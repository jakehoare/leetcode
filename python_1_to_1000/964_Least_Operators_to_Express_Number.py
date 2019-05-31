_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/least-operators-to-express-number
# Given a single positive integer x, we will write an expression of the form x (op1) x (op2) x (op3) x ... where each
# operator op1, op2, etc. is either addition, subtraction, multiplication, or division (+, -, *, or /).
# For example, with x = 3, we might write 3 * 3 / 3 + 3 - 3 which is a value of 3.
# When writing such an expression, we adhere to the following conventions:
# The division operator (/) returns rational numbers.
# There are no parentheses placed anywhere.
# We use the usual order of operations: multiplication and division happens before addition and subtraction.
# It's not allowed to use the unary negation operator (-).
# For example, "x - x" is a valid expression as it only uses subtraction, but "-x + x" is not because it uses negation.
# Write an expression with the least number of operators such that the expression equals the given target.
# Return the least number of operators used.

# Build the target as a number in base x, starting from the least significant digit.
# For each digit, we can either make the digit as a sum of ones (each one being made from x / x), or make the next
# power of x minus the digit.
# Apart from the first digit, subsequent digits are made as a power multiplied by the digits and possibly with an
# additional factor of power and the previous neg result.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def leastOpsExpressTarget(self, x, target):
        """
        :type x: int
        :type target: int
        :rtype: int
        """
        pos = neg = powers = 0

        while target:
            target, remainder = divmod(target, x)       # remainder is the next digit to be built in base x

            if powers == 0:
                pos, neg = remainder * 2, (x - remainder) * 2   # make digit or x - digit
            else:
                pos, neg = min(remainder * powers + pos, (remainder + 1) * powers + neg), \
                           min((x - remainder) * powers + pos, (x - remainder - 1) * powers + neg)

            powers += 1

        return min(pos, powers + neg) - 1   # add the final power to neg, subtract 1 since no final operator