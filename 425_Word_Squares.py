_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/word-squares/
# Given a set of words (without duplicates), find all word squares you can build from them.
# A sequence of words forms a valid word square if the kth row and column read the exact same string.
# All words will have the exact same length.

# Build a mapping of each prefix to all words that have that prefix. For each starting word, find all words with
# appropriate prefixes to build next row of square.
# Time - O((nk)**k) where k = len(word). For each of n words, calculate prefix of max length k, then recurse n times.
# Space - O(nk)

from collections import defaultdict

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        prefixes = defaultdict(list)
        for word in words:
            for i in range(1, len(word)):           # create all non-empty prefixes (excluding full word)
                prefixes[word[:i]].append(word)

        squares = []
        for word in words:
            self.build_square([word], prefixes, squares)    # try all words in first row
        return squares


    def build_square(self, partial, prefixes, squares):

        if len(partial) == len(partial[0]):                 # complete square
            squares.append(list(partial))                   # copy partial
            return

        prefix = []
        col = len(partial)
        for row in range(len(partial)):
            prefix.append(partial[row][col])
        next_words = prefixes["".join(prefix)]

        for next_word in next_words:
            partial.append(next_word)
            self.build_square(partial, prefixes, squares)
            partial.pop()       # remove next_word
