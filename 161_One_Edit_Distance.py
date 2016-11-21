_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/one-edit-distance/
# Given two strings s and t, determine if they are both one edit distance apart.

# If same lengths find the one different char (replacement edit) and test all else are same.
# If length diff of 1, find the extra char in longer and check all else is the same.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        diff = len(s) - len(t)
        if abs(diff) > 1:       # early break
            return False

        edit = False
        if diff == 0:           # one replacement
            for c_s, c_t in zip(s, t):
                if c_s != c_t:
                    if edit:    # already seen a replacement
                        return False
                    edit = True
            return edit         # False if no replacement

        else:                   # abs(diff) == 1
            long, short = s, t
            if diff < 0:
                long, short = short, long
            i = 0               # find the mismatch
            while i < len(short) and long[i] == short[i]:
                i += 1
            return long[i+1:] == short[i:]  # remainders must be same