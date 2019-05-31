_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/regular-expression-matching/
# Implement regular expression matching with support for '.' and '*'.
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Dynamic programming calculation of matrix of whether any prefix of s patches any prefix of p.
# Time - O(m*n) when m = len(p) and n = len(s)
# Space - O(m*n)

class Solution(object):
    def isMatch(self, s, p):

        # matched[i][j] is True if the first i chars of s (i.e. s[:i]) matches the first j chars of p (i.e. p[:j])
        matched = [[False for _ in range(len(p)+1)] for _  in range(len(s)+1)]
        matched[0][0] = True        # no pattern (j=0) matches no string and not any non-zero string

        for i in range(len(s)+1):
            for j in range(1, len(p)+1):
                pattern = p[j-1]

                if pattern == '.':      # dot matches any last character of s
                    matched[i][j] = (i != 0 and matched[i-1][j-1])

                elif pattern == '*':    # either ignore last 2 chars of p, or ignore last char of s provided it
                    star = p[j-2]       # matches the star char
                    matched[i][j] = matched[i][j-2] or (i > 0 and matched[i-1][j] and (star == s[i-1] or star == '.'))

                else:                   # pattern must match the last character of s
                    matched[i][j] = (i != 0 and matched[i-1][j-1] and s[i-1] == pattern)

        return matched[-1][-1]
