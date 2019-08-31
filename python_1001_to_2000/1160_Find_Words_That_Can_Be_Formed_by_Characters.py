_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
# You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars (each character can only be used once).
# Return the sum of lengths of all good strings in words.

# Count the chars.
# For each char of each word, if there are more instances of that char in the word than in chars,
# we cannot make the word.
# Time - O(m + n), length of chars + lengths of all words
# Space - O(m)

from collections import Counter

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        chars_count = Counter(chars)
        result = 0

        for word in words:
            for c in set(word):         # each unique char in word
                if word.count(c) > chars_count[c]:
                    break
            else:
                result += len(word)

        return result
