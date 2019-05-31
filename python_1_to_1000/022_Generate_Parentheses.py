_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/generate-parentheses/
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Recursively add an opening left bracket if any remain, and a closing right bracket if more left brackets have been used.
# Time - O(2^n), each recursion can generate 2 recursive calls althougn in practive this is an upper bound
# Space - O(2^n)

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generate([], n, n, result)
        return result

    # Generates all parentheses given a starting prefix and remaining left and right brackets.
    def generate(self, prefix, left, right, result):
        if left == 0 and right == 0:
            result.append("".join(prefix))
        if left != 0:
            self.generate(prefix + ['('], left-1, right, result)
        if right > left:
            self.generate(prefix + [')'], left, right-1, result)

