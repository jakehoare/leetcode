_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-word-in-dictionary/
# Given a list of strings words representing an English Dictionary, find the longest word in words that can be built
# one character at a time by other words in words. If there is more than one possible answer, return the longest word
# with the smallest lexicographical order.
# If there is no answer, return the empty string.

# Map lengths of words to sets of words with the same length.
# For each word longer than the current candidates (initially only the empty string is a candidate), add word to
# next_candidates if its prefix without final letter is already a candidate.
# Alternatively, for each word better than the longest word already found, check all prefixes in set of dictionary.
# Time - O(nk) for n words of maximum length k
# Space - O(nk)

from collections import defaultdict

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        length_to_words = defaultdict(set)

        for word in words:      # map word lengths to set of words
            length_to_words[len(word)].add(word)

        candidates = {""}       # initial candidate is the empty string
        length = 0              # length of current candidates

        while True:

            next_candidates = set()

            for longer_word in length_to_words[length + 1]: # check if each longer word can be built from any candidate
                if longer_word[:-1] in candidates:
                    next_candidates.add(longer_word)

            if not next_candidates:
                return sorted(list(candidates))[0]          # sort to return lexicographically lowest

            length += 1
            candidates = next_candidates