_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/ternary-expression-parser/
# Given a string representing arbitrarily nested ternary expressions, calculate the result of the expression. You can
# always assume that the given expression is valid and only consists of digits 0-9, ?, :, T and F.
# Each number will contain only one digit.
# The conditional expressions group right-to-left (as usual in most languages).
# The condition will always be either T or F. That is, the condition will never be a digit.
# The result of the expression will always evaluate to either a digit 0-9, T or F.

# Move form left to right adding all chars to a stack unless top of stack is '?'. In which case pop off true_val and
# false_val, then push back to stack result depending on current char.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack = []

        for c in expression[::-1]:

            if stack and stack[-1] == "?":
                stack.pop()     # remove '?'
                true_val = stack.pop()
                stack.pop()     # remove ':'
                false_val = stack.pop()
                if c == "T":
                    stack.append(true_val)
                else:
                    stack.append(false_val)

            else:
                stack.append(c)

        return stack.pop()