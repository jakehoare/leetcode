_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/word-pattern/
# Given a pattern and a string str, find if str follows the same pattern.
# Here follow means a full match, so that there is a bijection between a letter in pattern and a non-empty word in str.
# You may assume pattern contains only lowercase letters and str contains lowercase letters separated by a single space.

# Iterate over pairs of pattern chars and words, creating 2 mappings from pattern char to word and word to pattern
# char. If a word or pattern char has been mapped differently already then return False.
# Time - O(m + n)
# Space - O(m + n)

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        if len(str) != len(pattern):        # early return if lengths do not match
            return False

        p_to_s, s_to_p = {}, {}

        for w, c in zip(str, pattern):

            if c in p_to_s and p_to_s[c] != w:
                return False
            p_to_s[c] = w

            if w in s_to_p and s_to_p[w] != c:
                return False
            s_to_p[w] = c

        return True