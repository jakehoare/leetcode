_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/
# Given a function  f(x, y) and a value z, return all positive integer pairs x and y where f(x,y) == z.
# The function is constantly increasing, i.e.:
# f(x, y) < f(x + 1, y)
# f(x, y) < f(x, y + 1)
# The function interface is defined like this:
# interface CustomFunction {
# public:
#   // Returns positive integer f(x, y) for any given positive integer x and y.
#   int f(int x, int y);
# };
# For custom testing purposes you're given an integer function_id and a target z as input,
# where function_id represent one function from an secret internal list.
# You may return the solutions in any order.

# For each value of x, try all values of y until the function returns more than z.
# When it returns more than z, increment x and again try all values of y.
# Repeat for all values of x.
# Time - O(mn)
# Space - O(1)

class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        result = []

        for i in range(1, 101):
            for j in range(1, 101):
                temp = customfunction.f(i, j)
                if temp == z:
                    result.append([i, j])
                elif temp > z:
                    break

        return result
