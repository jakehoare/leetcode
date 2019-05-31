_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/permutation-in-string/
# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
# In other words, one of the first string's permutations is the substring of the second string.
# The input strings only contain lower case letters.

# Count frequencies of letters in s1 in an array. Slide window of length len(s1) over s2. Array maintains balance of
# counts in s1 - counts in window.
# Time - O(m + n), sum of string lengths
# Space - O(1)

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1 = len(s1)
        freq = [0] * 26     # counts of each char

        for c in s1:
            freq[ord(c) - ord("a")] += 1

        for i, c in enumerate(s2):

            freq[ord(c) - ord("a")] -= 1    # decrement count of letter added to window
            if i >= n1:
                freq[ord(s2[i - n1]) - ord("a")] += 1   # increment count of letter exiting window

            if not any(freq):
                return True

        return False