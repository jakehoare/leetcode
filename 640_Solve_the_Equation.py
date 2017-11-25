_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/solve-the-equation/
# Solve a given equation and return the value of x in the form of string "x=#value".
# The equation contains only '+', '-' operation, the variable x and its coefficient.
# If there is no solution for the equation, return "No solution".
# If there are infinite solutions for the equation, return "Infinite solutions".
# If there is exactly one solution for the equation, we ensure that the value of x is an integer.

# On each iteration of while loop, 1) identify any sign,  2) parse num or set to 1 if None, 3) add to total of x or val.
# When equals sign is found, reverse base to subtract counts on RHS of equals from LHS.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        x, val = 0, 0   # count of x and sum of integers
        base = 1        # set to -1 after seeing "="

        i = 0
        while i < len(equation):

            neg = base
            if equation[i] == "+":
                i += 1
            if equation[i] == "-":
                neg = -base
                i += 1

            num = None
            while i < len(equation) and "0" <= equation[i] <= "9":
                if num is None:
                    num = 0
                num = num * 10 + int(equation[i])
                i += 1

            if num is None:
                num = 1

            if i < len(equation) and equation[i] == "x":
                x += num * neg
                i += 1
            else:
                val += num * neg

            if i < len(equation) and equation[i] == "=":
                base *= -1
                i += 1

        if x == 0 and val == 0:
            return "Infinite solutions"
        if x == 0:
            return "No solution"
        return "x=" + str(-val // x)