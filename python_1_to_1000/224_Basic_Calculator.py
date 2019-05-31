_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/basic-calculator/
# Implement a basic calculator to evaluate a simple expression string.
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative
# integers and empty spaces .  You may assume that the given expression is always valid.

# Preprocess string to identify integers.  Recursively apply operator and bracket expression to previous result.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = {str(i) for i in range(10)}
        expression = ['(']      # wrap whole expression with brackets, easily identifies end

        for c in s:             # pre-process string into list of operators, brackets and ints
            if c == ' ':        # ignore blanks
                continue
            if c not in digits: # operator or bracket
                expression.append(c)
            elif isinstance(expression[-1], int):   # extending integer
                expression[-1] = expression[-1]*10 + int(c)
            else:                                   # new integer
                expression.append(int(c))

        expression.append(')')
        result, _ = self.evaluate(expression, 1)
        return result


    def evaluate(self, expression, i):      # evaluate from index i onwards to closing bracket

        calc, operator = 0, '+'
        while expression[i] != ')':

            atom = expression[i]
            if atom == '+' or atom == '-':  # store the operator
                operator = atom
            else:                           # open bracket or integer
                if isinstance(atom, int):
                    num = atom
                else:                       # recurse on bracketed expression
                    num, i = self.evaluate(expression, i+1)

                if operator == '+':         # apply operator to num
                    calc += num
                else:
                    calc -= num
            i += 1

        return calc, i      # return calculation and index of closing bracket