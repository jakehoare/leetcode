_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/valid-parenthesis-string/
# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this
# string is valid. We define the validity of a string by these rules:
# 1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# 2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
# 3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# 4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# 5. An empty string is also valid.

# Track the range of possible open brackets when iterating over s. If "(" is seen, both bounds of range increase. If
# ")" is seen both bounds decrease subject to the lower bound not becoming negative. If "*" is seen, upper bound
# increase and lower bound decreases, subject to zero. Upper bound can never be less than zero. Lower bound must be
# zero at end of s.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        min_open, max_open = 0, 0

        for c in s:

            if c == "(":
                min_open += 1
                max_open += 1
            elif c == ")":
                min_open = max(0, min_open - 1)
                max_open -= 1
            else:
                min_open = max(0, min_open - 1)
                max_open += 1

            if max_open < 0:
                return False

        return min_open == 0
