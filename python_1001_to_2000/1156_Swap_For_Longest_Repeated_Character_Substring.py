_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/swap-for-longest-repeated-character-substring/
# Given a string text, we are allowed to swap two of the characters in the string.
# Find the length of the longest substring with repeated characters.

# For each char, make a list of the start and end indices of substrings containing only that char.
# For each list of substrings, we can update the result with:
# - the substring length (no swap) if there are no other substrings with this char
# - the length + 1, if there is another substring
# - the sum of adjacent substrings, if the gap between them is one char
# - the sum of adjacent substrings + 1, if the gap between them is one char and there is at least one other substring
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        char_substrings = defaultdict(list)     # map char to list of [start, end] substrings
        for i, c in enumerate(text):
            if i == 0 or c != text[i - 1]:
                char_substrings[c].append([i, i])
            else:
                char_substrings[c][-1][1] = i

        result = 0
        for substrings in char_substrings.values():
            for i, (start, end) in enumerate(substrings):
                length = end - start + 1
                # add 1 to length if there is at least one other substring
                result = max(length + int(len(substrings) >= 2), result)

                if i != 0 and substrings[i - 1][1] == start - 2:    # gap of 1 char to previous substring
                    prev_length = substrings[i - 1][1] - substrings[i - 1][0] + 1
                    # move a char from another substring to fill the gap, else move from the end of one substring
                    result = max(result, length + prev_length + int(len(substrings) >= 3))

        return result
