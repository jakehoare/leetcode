_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sentence-similarity/
# Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs,
# determine if two sentences are similar.
# For example, "great acting skills" and "fine drama talent" are similar, if the similar word pairs are pairs =
# [["great", "fine"], ["acting","drama"], ["skills","talent"]].
# Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar, and "fine"
# and "good" are similar, "great" and "good" are not necessarily similar.
# However, similarity is symmetric. E.g., "great" and "fine" means that "fine" and "great" are similar.
# Also, a word is always similar with itself.
# Finally, sentences can only be similar if they have the same number of words.

# Create a mapping from a word to the set of similar words. Check each word of words1 against the word of the same
# index in words2 and vica versa. If words are same, continue.
# Else if there is no mapping between the words, return False.
# Time - O(m + n), len(pairs) + len(words)
# Space - O(m)

from collections import defaultdict

class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False

        similar = defaultdict(set)
        for w1, w2 in pairs:
            similar[w1].add(w2)             # map one way only

        for w1, w2 in zip(words1, words2):

            if w1 == w2:                    # samewords are always similar
                continue

            if (w1 not in similar or w2 not in similar[w1]) and (w2 not in similar or w1 not in similar[w2]):
                return False

        return True
