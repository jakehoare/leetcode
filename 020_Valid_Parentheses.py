_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/valid-parentheses/
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

# Maintain a stack of opening brackets.  For each closing bracket pop the head of the stack and check it matches.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match = {'(' : ')', '[' : ']', '{' : '}'}

        for c in s:
            if c in match:
                stack.append(c)
            else:
                if not stack or match[stack.pop()] != c:
                    return False

        return not stack
