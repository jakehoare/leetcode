_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/wildcard-matching/
# Implement wildcard pattern matching with support for '?' and '*'.
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

# Record index in p of star and index in s at that time.  Try to match without star, if fails back up and use *
# to match one more character from s.
# Time - O(m * n), * at beginning of p could match many chars in s before failing and repeatedly backtrack
# Space - O(1)

class Solution(object):
    def isMatch(self, s, p):

        i, j = 0, 0         # next indices to be matched in s and p
        star = -1           # last index in p of *

        while i < len(s):

            # if beyond end of pattern or pattern is unmatched letter
            if j >= len(p) or (p[j] not in {'*' , '?'} and p[j] != s[i]):
                if star == -1:      # no flexibility if no star
                    return False
                j = star + 1        # reset p to character after star
                star_i += 1         # reset s to charcater after star_i, i.e. use * to match one char from s
                i = star_i

            elif p[j] == '*':       # record * index in p and next index to be matched in s
                star = j
                star_i = i
                j += 1

            else:                   # chars match or ?, increment both
                i += 1
                j += 1

        while j < len(p):           # any remaining characters in p can only be *
            if p[j] != '*':
                return False
            j += 1
        return True

