_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/detect-capital/
# Given a word, you need to judge whether the usage of capitals in it is right or not.
# We define the usage of capitals in a word to be right when one of the following cases holds:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital if it has more than one letter, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.

# For the first and second letter, the only disallowed combination is lower case then upper case. All letter after
# the second character must be the same case as the second character.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 1:          # empty string or single letter
            return True

        first = word[0] <= "Z"
        second = word[1] <= "Z"
        if not first and second:    # first is not capital but second is
            return False

        for c in word[2:]:
            if (c <= "Z") != second:
                return False

        return True