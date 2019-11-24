_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-score-words-formed-by-letters/
# Given a list of words, list of  single letters (might be repeating) and score of every character.
# Return the maximum score of any valid set of words formed by using
# the given letters (words[i] cannot be used two or more times).
# It is not necessary to use all characters in letters and each letter can only be used once.
# Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

# Convert each word to a score.
# If we have insufficient letters to make the word, we can only get the score from the next word onwards.
# Else we can either make the word or not.
# If we make the word, reduce the counts of all letters in the word and recurse,
# then increment the counts after returning from recursion.
# Time - O(2 ** n)
# Space - O(n)

from collections import Counter

class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        char_counts = Counter(letters)      # counts of letters that can be used

        word_scores = []
        a = ord("a")
        for word in words:
            word_scores.append(sum(score[ord(c) - a] for c in word))

        def can_make(word_counts):          # is there sufficient remaining count to make a word?
            for c, count in word_counts.items():
                if c not in char_counts or char_counts[c] < count:
                    return False
            return True

        def helper(i):
            if i == len(words):
                return 0

            not_use = helper(i + 1)         # score if we do not use words[i], try i + 1

            word_counts = Counter(words[i])
            if not can_make(word_counts):
                return not_use              # cannot make this word

            for c, count in word_counts.items():
                char_counts[c] -= count     # decrement counts before recurse
            use = word_scores[i] + helper(i + 1)
            for c, count in word_counts.items():
                char_counts[c] += count     # increment counts after recurse

            return max(use, not_use)

        return helper(0)
