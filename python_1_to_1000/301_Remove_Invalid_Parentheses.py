_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-invalid-parentheses/
# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
# The input string may contain letters other than the parentheses ( and ).

# When there are more closing than opening brackets, remove any previous closing bracket at the last removed position
# or without a closing bracket before it (to avoid duplicate solutions) and recurse for remainder of string.  If
# string is then valid, reverse string and switch opening and closing brackets to repeat in other direction.

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        valid = []
        self.remove(s, valid, 0, 0, ('(', ')'))
        return valid


    def remove(self, s, valid, start, removed,  par):
        net_open = 0

        for i in range(start, len(s)):
            net_open += ((s[i] == par[0]) - (s[i] == par[1]))
            if net_open >= 0:
                continue

            # string is invalid so remove a closing bracket
            for j in range(removed, i+1):
                if s[j] == par[1] and (j == removed or s[j - 1] != par[1]):
                    self.remove(s[:j] + s[j+1:], valid, i, j, par)
            return

        reversed = s[::-1]
        if par[0] == '(':       # finished left to right
            self.remove(reversed, valid, 0, 0, (')', '('))
        else:                   # finished right to left
            valid.append(reversed)

