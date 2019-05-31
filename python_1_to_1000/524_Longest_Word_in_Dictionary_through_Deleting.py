_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
# Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting
# some characters of the given string. If there are more than one possible results, return the longest word with the
# smallest lexicographical order. If there is no possible result, return the empty string.

# Sort by length then by lexicogrphic order. For each string from longest, test if is a subsequence of s.
# Time - O(mn + knlogn) where knlogn is time taken to sort for n strings and s is of length m
# Space - O(1)

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """

        def is_subsequence(s, t):  # return True if s is a subsequence of t
            i, j = 0, 0
            while i < len(s) and (len(t) - j) >= (len(s) - i):  # nb chars remaining in t >= nb chars remaining in s
                if s[i] == t[j]:
                    i += 1
                j += 1
            if i == len(s):
                return True
            return False

        d.sort(key=lambda x: (-len(x), x))      # primary and secondary keys

        for word in d:
            if is_subsequence(word, s):
                return word

        return ""