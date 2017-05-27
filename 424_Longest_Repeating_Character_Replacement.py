_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-repeating-character-replacement/
# Given a string that consists of only uppercase English letters, you can replace any letter in the string with another
# letter at most k times. Find the length of a longest substring containing all repeating letters you can get after
# performing the above operations.

# Maintain a sliding window, moving end forwards every iteration. Move start forwards so that there are at most k chars
# in the window that are not the most frequent.
# Time - O(n)
# Space - O(1)

from collections import defaultdict

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        longest, start = 0, 0
        freq = defaultdict(int)

        for end in range(len(s)):
            freq[s[end]] += 1
            # while more than k chars in window that are not the most frequent
            while (end - start + 1) - max(freq.values()) > k:
                freq[s[start]] -= 1
                start += 1

            longest = max(longest, end - start + 1)

        return longest
