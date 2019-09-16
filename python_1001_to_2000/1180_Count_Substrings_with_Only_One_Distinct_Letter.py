_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/
# Given a string S, return the number of substrings that have only one distinct letter.

# Iterate along S, tracking the start of the current sequence of identical letters.
# If a char if different from the previous, then update the previous and the start.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def countLetters(self, S):
        """
        :type S: str
        :rtype: int
        """
        previous = "#"
        start = 0
        substrings = 0

        for end, c in enumerate(S):
            if c != previous:
                start = end
                previous = c
            substrings += end - start + 1   # add all substrings with current end

        return substrings
