_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
# You are given a string s that consists of lower case English letters and brackets.
# Reverse the strings in each pair of matching parentheses, starting from the innermost one.
# Your result should not contain any brackets.

# Iterate along s, maintaining a stack of text at each depth of open braces.
# For an opening brace, add the text since the previous brace to the current stack top and start a new stack level.
# For a closing brace, add the text since the previous brace to the current stack top, then pop the top, reverse it
# and add to the new stack top.
# Time - O(n**2)
# Space - O(n)

class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [""]

        start = 0
        for i, c in enumerate(s):
            if c == "(":        # add substring to top of stack and start a new empty substring
                stack[-1] += s[start:i]
                stack.append("")
                start = i + 1
            elif c == ")":
                stack[-1] += s[start:i]
                stack[-1] += stack.pop()[::-1]
                start = i + 1

        return stack[0] + s[start:]     # add remaining text
