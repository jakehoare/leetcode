_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-valid-parentheses/
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
# For example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

# Maintain a stack of indices in s of unmatched brackets.  Pop an opening bracket when matched with a closing bracket.
# Push unmatched closing brackets and all opening brackets.  Then find the longest gap between indices on the stack.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []                  # indices of brackets that are not matched

        for i, c in enumerate(s):
            if c == ")" and stack and s[stack[-1]] == '(':
                stack.pop()         # close matches an open on the stack
            else:
                stack.append(i)     # puch open brackets or unmatched close brackets

        stack.append(len(s))        # last unmatched index after end of s
        max_length = stack[0]       # first unmatched index before start of s

        for index in range(1, len(stack)):  # find max gap between remaining unmatched indices
            max_length = max(max_length, stack[index] - stack[index-1] - 1)

        return max_length

