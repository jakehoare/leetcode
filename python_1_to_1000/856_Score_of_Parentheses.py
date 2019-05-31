_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/score-of-parentheses/
# Given a balanced parentheses string S, compute the score of the string based on the following rule:
# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.

# Maintain a stack of opening brackets and the score within each opening bracket. When we see a closing bracket,
# either add or append 1, or multiply the previous top of stack by 2.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []                  # opening brackets, followed by the score within that open bracket

        for s in S:

            if s == "(":
                stack.append(s)

            else:                   # closing bracket
                item = stack.pop()
                if item == "(":     # matched pair of "()"
                    num = 1
                else:               # item is an integer
                    stack.pop()     # discard opening bracket before integer
                    num = 2 * item

                if stack and stack[-1] != "(":  # add if top of stack is a num, else append
                    stack[-1] += num
                else:
                    stack.append(num)

        return stack[0]
