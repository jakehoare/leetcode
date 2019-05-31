_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/basic-calculator-iv/
# Given an expression such as expression = "e + 8 - a + 5" and an evaluation map such as {"e": 1}
# (given in terms of evalvars = ["e"] and evalints = [1]), return a list of tokens representing the simplified
# expression, such as ["-1*a","14"]
# An expression alternates chunks and symbols, with a space separating each chunk and symbol.
# A chunk is either an expression in parentheses, a variable, or a non-negative integer.
# A variable is a string of lowercase letters (not including digits.) Note that variables can be multiple letters,
# and note that variables never have a leading coefficient or unary operator like "2x" or "-x".
# Expressions are evaluated in the usual order: brackets first, then multiplication, then addition and subtraction.
# For example, expression = "1 + 2 * 3" has an answer of ["7"].
# The format of the output is as follows:
# For each term of free variables with non-zero coefficient, we write the free variables within a term in sorted
# order lexicographically. For example, we would never write a term like "b*a*c", only "a*b*c".
# Terms have degree equal to the number of free variables being multiplied, counting multiplicity.
# (For example, "a*a*b*c" has degree 4.) We write the largest degree terms of our answer first, breaking ties by
# lexicographic order ignoring the leading coefficient of the term.
# The leading coefficient of the term is placed directly to the left with an asterisk separating it from the variables
# (if they exist.)  A leading coefficient of 1 is still printed.
# An example of a well formatted answer is ["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"]
# Terms (including constant terms) with coefficient 0 are not included.
# For example, an expression of "0" has an output of [].

# Create a class that extends Counter by using a __mul__ method.
# Time - O(2**n + m) where len(expression) == n and len(evalvars) == m
# Space - O(n + m)

from collections import Counter
import re

class Solution(object):
    def basicCalculatorIV(self, expression, evalvars, evalints):
        """
        :type expression: str
        :type evalvars: List[str]
        :type evalints: List[int]
        :rtype: List[str]
        """

        class CounterMul(Counter):

            def __add__(self, other):
                self.update(other)
                return self

            def __sub__(self, other):
                self.subtract(other)
                return self

            def __mul__(self, other):
                product = CounterMul()
                for x in self:
                    for y in other:
                        xy = tuple(sorted(x + y))
                        product[xy] += self[x] * other[y]
                return product

        vals = dict(zip(evalvars, evalints))        # mapping of variables to values

        def make_counter(token):

            token = str(vals.get(token, token))     # get mapping or return same token

            if token.isalpha():
                return CounterMul({(token,): 1})    # map token to count of one
            return CounterMul({(): int(token)})     # map empty tuple to integer

        # wrap all tokens with a call to make_counter and evaluate to aggregate
        counter = eval(re.sub('(\w+)', r'make_counter("\1")', expression))
        # '(\w+)' matches groups of 1 or more alphanumeric
        # r'make_counter("\1")' uses \1 to to signify the matched groups and r so that \ is not special

        # sort keys by decreasing length then lexicographically
        sorted_terms = sorted(counter, key=lambda x: (-len(x), x))

        result = []
        for term in sorted_terms:
            if counter[term]:                       # ignore zero values
                result.append("*".join((str(counter[term]),) + term))

        return result