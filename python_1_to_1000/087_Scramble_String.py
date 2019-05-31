_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/scramble-string/
# Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
# To scramble the string, we may choose any non-leaf node and swap its two children.
# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

# Base cases of strings containing different characters or same string.  Else for all partition points, lest and right
# sides are scrambled versions, before or after swapping.
# Time - exponential since 4n recursive calls for string of length n.

from collections import Counter

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        count1 = Counter(s1)
        for c in s2:
            if c not in count1:
                return False
            count1[c] -= 1
            if count1[c] < 0:
                return False

        if s1 == s2:
            return True

        for partition in range(1, len(s1)):

            s1_l = s1[:partition]       # partition number of chars from left
            s1_r = s1[partition:]       # last (len(s1) - partition) chars
            s2_l = s2[:partition]
            s2_r = s2[partition:]
            s2_l_swap = s2[:-partition] # (len(s2) - partition) chars from left
            s2_r_swap = s2[-partition:] # last partition chars

            if (self.isScramble(s1_l, s2_l) and self.isScramble(s1_r, s2_r)) or \
                    (self.isScramble(s1_l, s2_r_swap) and self.isScramble(s1_r, s2_l_swap)):
                return True

        return False
