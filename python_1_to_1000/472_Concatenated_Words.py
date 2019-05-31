_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/concatenated-words/
# Given a list of words (without duplicates), please write a program that returns all concatenated words in the given
# list of words. A concatenated word is defined as a string that is comprised entirely of at least two shorter words
# in the given array.

# For each prefix of each word, if prefix is a word test whether suffix is a word or a concatenation of words
# Time - O(n * k**2) for n words of max length k
# Space - O(k)

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        def is_concat(word):
            if not word or word in word_set:    # word will not be empty on first call
                return True

            for i in range(1, len(word) + 1):  # check to end of word
                if word[:i] in word_set and is_concat(word[i:]):
                    return True

            return False

        word_set = set(words)
        results = []
        for word in words:
            for i in range(1, len(word)):  # prefix/suffix where prefix is in dict and suffix is not empty
                if word[:i] in word_set and is_concat(word[i:]):
                    results.append(word)
                    break
        return results