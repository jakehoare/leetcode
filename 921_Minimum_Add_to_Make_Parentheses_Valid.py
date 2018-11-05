_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/inimum-add-to-make-parentheses-valid/
# Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')',
# and in any positions ) so that the resulting parentheses string is valid.
# Formally, a parentheses string is valid if and only if:
# It is the empty string, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

# Track net balance of open minus closed brackets. Add an opening bracket whenever the balance is negative, because
# there cannot be more closed than open brackets. At the end, add closing brackets for all open brackets.
# Time - O(n)
# Space - O(1)

class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        additions = 0               # number of brackets added
        net_open = 0                # balance of opening brackets minus closing brackets

        for c in S:

            net_open += 1 if c == "(" else -1   # update the net_open balance

            if net_open == -1:      # more closing than opening, add an opening bracket
                additions += 1
                net_open = 0

        return additions + net_open # close all remaining open brackets