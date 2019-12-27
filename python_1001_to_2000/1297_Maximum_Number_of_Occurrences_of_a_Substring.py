_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/
# Given a string s, return the maximum number of occurrences of any substring under the following rules:
# The number of unique characters in the substring must be less than or equal to maxLetters.
# The substring size must be between minSize and maxSize inclusive.

# Ignore maxSize since there will be most substrings of length minSize.
# Maintain a sliding window of length minSize, counting the frequency of each letter in the window.
# Update the window with each end letter.
# If window is of length >= minSise then check if window has <= maxLetters, then remove start letter.
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        substrings = defaultdict(int)   # map substring to its count in s
        letters = defaultdict(int)      # map letter to its count in sliding window

        for end in range(len(s)):
            letters[s[end]] += 1        # add letter to window count before checking substring
            start = end - minSize + 1
            if start >= 0:
                if len(letters) <= maxLetters:  # increment substring count if <= maxLetters in window
                    substrings[s[start:end + 1]] += 1
                letters[s[start]] -= 1  # remove letter from window count after checking substring
                if letters[s[start]] == 0:
                    del letters[s[start]]

        return 0 if not substrings else max(substrings.values())
