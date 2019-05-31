_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
# Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

# Maintain a window of the longest substring.  If a 3rd char is found, reset the window start to after the first
# seen char.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, max_substring = 0, 0
        last_seen = {}                  # key is char, value is last index of char

        for i, c in enumerate(s):

            if c in last_seen or len(last_seen) < 2:    # extend substring with same start
                max_substring = max(max_substring, i - start + 1)

            else:           # c not in current substring and 2 chars seen
                for seen in last_seen:
                    if seen != s[i-1]:              # find the char that is not the previous char
                       start = last_seen[seen] + 1  # move start to after this char
                       del last_seen[seen]
                       break

            last_seen[c] = i

        return max_substring

