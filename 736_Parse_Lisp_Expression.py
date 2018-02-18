_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/parse-lisp-expression/
# You are given a string expression representing a Lisp-like expression to return the integer value of.
# The syntax for these expressions is given as follows.
# An expression is either an integer, a let-expression, an add-expression, a mult-expression, or an assigned variable.
# Expressions always evaluate to a single integer. (An integer could be positive or negative.)
# A let-expression takes the form (let v1 e1 v2 e2 ... vn en expr), where let is always the string "let", then there
# are 1 or more pairs of alternating variables and expressions, meaning that the first variable v1 is assigned the
# value of the expression e1, the second variable v2 is assigned the value of the expression e2, and so on
# sequentially; and then the value of this let-expression is the value of the expression expr.
# An add-expression takes the form (add e1 e2) where add is always the string "add", there are always two
# expressions e1, e2, and this expression evaluates to the addition of the evaluation of e1 and the evaluation of e2.
# A mult-expression takes the form (mult e1 e2) where mult is always the string "mult", there are always two
# expressions e1, e2, and this expression evaluates to the multiplication of the evaluation of e1 and the evaluation
# of e2.
# For the purposes of this question, we will use a smaller subset of variable names. A variable starts with a
# lowercase letter, then zero or more lowercase letters or digits. Additionally for your convenience, the names
# "add", "let", or "mult" are protected and will never be used as variable names.
# Finally, there is the concept of scope. When an expression of a variable name is evaluated, within the context of
# that evaluation, the innermost scope (in terms of parentheses) is checked first for the value of that variable,
# and then outer scopes are checked sequentially. It is guaranteed that every expression is legal.

# Split the input by spaces. This gives a list of tokens, which may be operators, variables or integers. Brackets
# may be present before or after a token.
# Create a stack of dictionaries. The top of the stack is dictionary mapping variables to their values in the current
# scope.
# The helper function takes an index in the list of tokens and returns the value of the expression from that token
# until the corresponding closing bracket. It also return the index of the next token after the closing bracket.
# The helper function first removes any opening bracket from the the current token. If there is an opening bracket then
# we have moved up a level of scope, so copy all the previous variables in scope into a new dictionary.
# Count and remove the closing brackets.
# Then there are 5 cases:
#  Integer - return its value.
#  Add - parse the next expression and subsequent expression then add them.
#  Mult - parse the next expression and subsequent expression then multiply them them.
#  Let - for every pair of variable / expression, map the variable to the evaluates expression's value. The continue_let
#   function determines whether this is the final expression to be returned.
#  Variable - find its value from the mapping.
# Along with the return value we always also return the index of the next token to parse.
# Before returning we pop off and discard any scopes that are removed due to closing brackets.
# Time - O(n)
# Space - O(n**2), dictionaries may repeat the same variable

class Solution(object):
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        tokens = expression.split(" ")          # list of operators, variables and integers
        scopes = [{}]                           # stack of dictionaries

        def helper(start):                      # returns (value of expression, next index to parse)

            if start >= len(tokens):            # base case
                return 0, start

            operator = tokens[start]
            if operator[0] == "(":              # remove opening bracket if any
                operator = operator[1:]
                scopes.append(dict(scopes[-1])) # move up a level of scope, including all previous variables

            closing_brackets = 0
            while operator[len(operator) - 1 - closing_brackets] == ")":    # remove and count closing brackets if any
                closing_brackets += 1
            if closing_brackets > 0:
                operator = operator[:-closing_brackets]

            if operator.isdigit() or operator[0] == "-" and operator[1:].isdigit():
                result = int(operator), start + 1

            elif operator == "add":
                left, next_i = helper(start + 1)
                right, next_i = helper(next_i)
                result = (left + right, next_i)

            elif operator == "mult":
                left, next_i = helper(start + 1)
                right, next_i = helper(next_i)
                result = (left * right, next_i)

            elif operator == "let":
                next_i = start + 1
                while continue_let(next_i):
                    variable = tokens[next_i]
                    expression, next_i = helper(next_i + 1)
                    scopes[-1][variable] = expression
                result =  helper(next_i)

            else:                               # operator is variable
                result = (scopes[-1][operator], start + 1)

            while closing_brackets > 0:         # remove old scopes
                closing_brackets -= 1
                scopes.pop()

            return result

        # Determines whether we should continue parsing pairs of var/expression for let operator
        def continue_let(i):                    # test for variable without closing bracket
            return "a" <= tokens[i][0] <= "z" and tokens[i][-1] != ")"

        return helper(0)[0]
