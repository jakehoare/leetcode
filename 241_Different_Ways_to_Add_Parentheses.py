_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/different-ways-to-add-parentheses/
# Given a string of numbers and operators, return all possible results from computing all the different
# possible ways to group numbers and operators. The valid operators are +, - and *.

# Preprocess the string into a list of integers and string operators.  Split the string by each operators and
# recurse on the left and the right expressions.  Combine the left and the right results in all possible ways.
# Memoize the results to save duplication.

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        start = 0       # start index of current integer
        parsed = []

        for i in range(len(input)):
            if not input[i].isdigit():
                parsed.append(int(input[start:i]))      # append integer
                parsed.append(input[i])                 # append operator
                start = i+1
        parsed.append(int(input[start:len(input)]))

        return self.diff_ways(parsed, 0, len(parsed)-1, {})


    def diff_ways(self, s, left, right, memo):

        if left == right:       # case case of single integer
            return [s[left]]
        if (left, right) in memo:
            return memo[(left, right)]

        ways = []
        for i in range(left+1, right, 2):   # partiton by each operator

            left_results = self.diff_ways(s, left, i-1, memo)
            right_results = self.diff_ways(s, i+1, right, memo)

            for l in left_results:
                for r in right_results:
                    if s[i] == '+':
                        ways.append(l+r)
                    elif s[i] == '-':
                        ways.append(l-r)
                    elif s[i] == '*':
                        ways.append(l*r)

        memo[(left, right)] = ways
        return ways
