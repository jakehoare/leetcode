_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-string-chain/
# Given a list of words, each word consists of English lowercase letters.
# Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make
# it equal to word2.  For example, "abc" is a predecessor of "abac".
# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor
# of word_2, word_2 is a predecessor of word_3, and so on.
# Return the longest possible length of a word chain with words chosen from the given list of words.

# Sort the words in increasing order of length. For each word, make all shorter words by removing one char.
# If a shorter word is valid, we can extend its chain by adding this word.
# Save the best result from all shorter words.
# Time - O(n k**2) for n words of maximum length k
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        longest = defaultdict(int)

        for word in sorted(words, key=len):
            for i in range(len(word)):
                prev = longest[word[:i] + word[i + 1:]]         # result for word with word[i] removed
                longest[word] = max(longest[word], prev + 1)

        return max(longest.values())
