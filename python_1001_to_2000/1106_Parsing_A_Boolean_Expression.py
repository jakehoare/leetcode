_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/parsing-a-boolean-expression/
# Return the result of evaluating a given boolean expression, represented as a string.
# An expression can either be:
# "t", evaluating to True;
# "f", evaluating to False;
# "!(expr)", evaluating to the logical NOT of the inner expression expr;
# "&(expr1,expr2,...)", evaluating to the logical AND of 2 or more inner expressions expr1, expr2, ...;
# "|(expr1,expr2,...)", evaluating to the logical OR of 2 or more inner expressions expr1, expr2, ...

# Iterate over the expression.
# Add opening braces, booleans and operators to the stack, ignore commas.
# For closing braces, pop all booleans off and add to a set.
# Apply the operator to the set and push the result back onto the stack.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        stack = []

        for c in expression:
            if c == "t":
                stack.append(True)
            elif c == "f":
                stack.append(False)
            elif c == ")":
                booleans = set()
                while stack[-1] != "(":
                    booleans.add(stack.pop())
                stack.pop()             # discard opening bracket
                operator = stack.pop()
                if operator == "&":
                    stack.append(all(booleans))
                elif operator == "|":
                    stack.append(any(booleans))
                else:
                    stack.append(not booleans.pop())
            elif c != ",":
                stack.append(c)

        return stack[-1]
