_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/word-break/
# Given a string s and a dictionary of words dict, determine if s can be segmented into a
# space-separated sequence of one or more dictionary words.

# Dynamic programming.  A prefix can be made from words in dictionary if it can be split into a shorter prefix
# that can be made and another word in dictionary.
# Time - O(n**3), there are O(n**2) substrings s[j:i], each taking O(n) to create
# Space - O(n)

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        can_make = [False] * (len(s)+1)         # can_make[i] is True if can make prefix of length i
        can_make[0] = True

        for i in range(1, len(s)+1):            # prefix length
            for j in range(i-1, -1, -1):        # j is existing prefix, start with longest + shortest new word
                if can_make[j] and s[j:i] in wordDict:
                    can_make[i] = True
                    break

        return can_make[-1]
