_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/split-a-string-in-balanced-strings/
# Balanced strings are those who have equal quantity of 'L' and 'R' characters.
# Given a balanced string s split it in the maximum amount of balanced strings.
# Return the maximum amount of splitted balanced strings.

# Keep a running net balance of "L" - "R" when iterating over s.
# Update the result whenever the balance is zero.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        balance = 0
        result = 0

        for c in s:
            balance += 1 if c == "L" else -1
            if balance == 0:
                result += 1

        return result
