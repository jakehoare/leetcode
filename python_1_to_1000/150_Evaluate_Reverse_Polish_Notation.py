_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Push numbers onto stack.  Apply operators to top 2 members of stack and push back result.
# Faster but less concise without using eval().
# Time - O(n)
# Space - O(n)

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ops = {'+', '-', '/', '*'}
        stack = []

        for token in tokens:

            if token in ops:
                right = stack.pop()
                left = stack.pop()
                if token == '/':
                    stack.append(int(left / float(right)))      # round down
                else:
                    stack.append((eval(str(left) + token + str(right))))
            else:
                stack.append(int(token))

        return stack[-1]
