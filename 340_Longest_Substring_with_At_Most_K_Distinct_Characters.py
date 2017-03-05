_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# Given a string, find the length of the longest substring T that contains at most k distinct characters.

# Maintain that last index of each character seen in a sliding window.  Extend the window by adding a new character
# and if there are then more than k distinct characters, slide the start of the window forward until a char is removed.
# Time - O(n)
# Space - O(k)

from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start, longest = 0, 0
        last_seen = defaultdict(int)        # key is char, value is last index of key

        for end, c in enumerate(s):
            last_seen[c] = end                      # add c to mapping

            while len(last_seen) > k:               # too many distinct chars in s[start:end + 1]
                if last_seen[s[start]] == start:    # last_seen of start char is start index
                    del last_seen[s[start]]         # remove start char
                start += 1                          # move front of window forwards

            else:                           # longest can increase if have not entered while loop
                longest = max(longest, end - start + 1)

        return longest