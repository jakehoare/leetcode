_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-and-replace-pattern/
# You have a list of words and a pattern, and you want to know which words in words matches the pattern.
# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in
# the pattern with p(x), we get the desired word.
# Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter,
# and no two letters map to the same letter.
# Return a list of the words in words that match the given pattern.
# You may return the answer in any order.

# Each word and the pattern are converted to their canonical representations, which can then be compared.
# In a canonical representation, characters are mapped to integers in order of their appearance in the string.
# The first character is mapped to 0, as are all subsequent appearances of that character. The second unique character
# is mapped to 1, etc.
# Time - O(n) total length of all words and pattern
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def canonical(s):               # return a canonical representation of a string
            result = []                 # list of integers
            mapping = {}                # map char to value
            value = 0                   # next value (equal to number of unique chars seen)

            for c in s:
                if c not in mapping:    # create a new mapping if c has not been seen before
                    mapping[c] = value
                    value += 1
                result.append(mapping[c])
            return tuple(result)

        pattern = canonical(pattern)
        return [word for word in words if canonical(word) == pattern]
