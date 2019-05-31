_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-matching-subsequences/
# Given string S and a dictionary of words words, find the number of words[i] that are a subsequences of S.

# Maintain a mapping for each word from the next char to be matched to the remainder of the word. For each char in
# S, update the mapping by removing the key/value with the current char and adding the words back with keys of their
# chars to be matched.
# Time - O(m + n), len(S) + sum of all words
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        letter_to_suffixes = defaultdict(list)  # map next char of a word to suffix after that char
        letter_to_suffixes["#"] = words         # special character will be matched initially
        result = 0

        for c in "#" + S:

            suffixes = letter_to_suffixes[c]    # cannot pop unless checking whether c is in letter_to_suffixes
            del letter_to_suffixes[c]

            for suffix in suffixes:

                if len(suffix) == 0:            # matched all of this word
                    result += 1
                    continue

                next_letter, next_suffix = suffix[0], suffix[1:]
                letter_to_suffixes[next_letter].append(next_suffix)

        return result