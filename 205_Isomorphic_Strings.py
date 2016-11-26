_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/isomorphic-strings/
# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character but a character may map to itself.

# Store a mapping from chars of s to chars of t.  If a char in s is already in mapping then check that the char in t
# is same as previously observed.  Check also that a new mapping of char in s is not to a char in t already mapped.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_mapped = set()

        for cs, ct in zip(s, t):

            if cs in s_to_t:
                if s_to_t[cs] != ct:
                    return False
            elif ct in t_mapped:
                return False
            s_to_t[cs] = ct
            t_mapped.add(ct)

        return True
