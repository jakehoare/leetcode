_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/basic-calculator-iii/
# Implement a basic calculator to evaluate a simple expression string.
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers
# and empty spaces .
# The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses )
# and empty spaces. The integer division should truncate toward zero.
# You may assume that the given expression is always valid.

# Firstly, parse string to a list of integers, operators and sub-lists. Evaluate parsed list by creating a list of
# integers to be summed by using divide and multiply with the next and previous integers.
# Recursively calculate sub-lists.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operators = {"+", "-", "*", "/"}

        def parse(i):                                           # parse s from index i

            parsed = []

            while i < len(s):
                c = s[i]

                if c in operators:
                    parsed.append(c)
                elif "0" <= c <= "9":
                    if parsed and isinstance(parsed[-1], int):  # part of previous integer
                        parsed[-1] = parsed[-1] * 10 + int(c)
                    else:                                       # start a new integer
                        parsed.append(int(c))
                elif c == "(":
                    sublist, i = parse(i + 1)
                    parsed.append(sublist)
                elif c == ")":
                    return parsed, i                            # parsed sub-string and index to restart from

                i += 1                                          # ignores blank spaces

            return parsed, len(s)


        def calculate(tokens):

            if isinstance(tokens, int):                         # base case of single integer
                return tokens

            result = [calculate(tokens[0])]                     # list of integers

            for i in range(1, len(tokens), 2):                  # iterate over pairs of operator and integer
                op, num = tokens[i], calculate(tokens[i + 1])

                if op == "/":
                    result.append(result.pop() // num)
                elif op == "*":
                    result.append(result.pop() * num)
                elif op == "+":
                    result.append(num)
                else:
                    result.append(-num)

            return sum(result)

        parsed_s, _ = parse(0)
        return calculate(parsed_s)
