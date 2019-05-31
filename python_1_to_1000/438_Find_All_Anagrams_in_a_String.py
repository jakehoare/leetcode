_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
# The order of output does not matter.

# Maintain a count of each letter in a sliding window in s, minus the counts of letters in p. Populate the dictionary
# with the intial counts, then slide along removing chars at the back and adding chars at the front. Add to result if
# dictionary is empty (all values zero).
# Time - O(n) len(s)
# Space - O(m) len(p)

from collections import defaultdict

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(p)
        freq = defaultdict(int)     # map from char to net count of char in sliding window
        result = []

        if n > len(s):              # no anagrams are possible
            return result

        def update_freq(c, step):   # updates dictionary and deletes zero values
            freq[c] += step
            if freq[c] == 0:
                del freq[c]

        for c1, c2 in zip(p, s[:n]):    # populate initial window
            update_freq(c1, -1)
            update_freq(c2, 1)

        for i in range(len(s) - n):
            if not freq:
                result.append(i)
            update_freq(s[i], -1)       # remove char at back of window
            update_freq(s[i + n], 1)    # add char at front of window

        if not freq:
            result.append(len(s) - n)
        return result
