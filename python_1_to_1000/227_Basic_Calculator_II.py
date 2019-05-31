_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/basic-calculator-ii/
# Implement a basic calculator to evaluate a simple expression string.
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces.
# The integer division should truncate toward zero.
# You may assume that the given expression is always valid.

# Create a stack of partial results to be summed to get the full result.  Iterate over s.  When c is a digit
# increase the current integer num.  When c is an operator or at end of string, apply the previous operator
# to num.  For '*' and '/' this uses the previous integer on the stack.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        op = '+'

        for i, c in enumerate(s):

            if c.isdigit():                 # build num
                num = num*10 + int(c)

            if (not c.isdigit() and c != ' ') or i == len(s)-1:    # c is an operator or end of string
                if op == '+':               # use previous operator op
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                else:   # op == '/'
                    left = stack.pop()
                    stack.append(left // num)
                    if left // num < 0 and left % num != 0:
                        stack[-1] += 1      # # negative integre division result with remainder rounds down by default
                num = 0     # num has been used so reset
                op = c

        return sum(stack)