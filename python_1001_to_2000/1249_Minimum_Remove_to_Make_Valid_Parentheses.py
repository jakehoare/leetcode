_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# Given a string s of '(' , ')' and lowercase English characters.
# Your task is to remove the minimum number of parentheses ( '(' or ')',
# in any positions ) so that the resulting parentheses string is valid and return any valid string.
# Formally, a parentheses string is valid if and only if:
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

# Iterate along s, adding opening brackets to a list.
# If we see a closing bracket without any opening bracket, it must be removed.
# If we see a closing bracket with unmatched opening brackets, discard the matching opening bracket.
# Finally, discard any unmatched opening brackets before reconstructing s without discarded indices.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        opening = []                # indices of opening brackets
        removals = set()            # indices of removed brackets

        for i, c in enumerate(s):
            if c == "(":
                opening.append(i)
            elif c == ")":
                if not opening:     # no matching opening
                    removals.add(i)
                else:               # match with opening
                    opening.pop()

        removals.update(opening)    # add all open but not closed brackets
        return "".join(c for i, c in enumerate(s) if i not in removals)
