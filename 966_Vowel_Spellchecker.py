_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/vowel-spellchecker/
# Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.
#
# For a given query word, the spell checker handles two categories of spelling mistakes:
#
# Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with
# the same case as the case in the wordlist.
# Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
# Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
# Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
# Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually,
# it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the
# match in the wordlist.
# Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
# Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
# Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
# In addition, the spell checker operates under the following precedence rules:
#
# When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
# When the query matches a word up to capitlization, you should return the first such match in the wordlist.
# When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
# If the query has no matches in the wordlist, you should return the empty string.
# Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

# Create a set of the words for O(1) lookup. Map the lower case of each word to the first such word.
# Map the lower case with vowels replaced by underscore to the first such word.
# Look up each word in the set and both mappings, returning the first hit.
# Time - O(m + n)
# Space - O(m + n)

from re import sub

class Solution:
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """

        def replace_vowels(word):
            return sub('[aeiou]', '_', word)

        wordsset = set(wordlist)

        lower_words, vowel_words = {}, {}
        for word in wordlist:
            lower_words.setdefault(word.lower(), word)  # do not overwrite if key already exists
        for word in lower_words.keys():
            replaced = replace_vowels(word)
            vowel_words.setdefault(replaced, lower_words[word])

        def check(word):
            if word in wordsset:
                return word

            low = word.lower()
            result = lower_words.get(low, "")       # return empty string if not found
            if result == "":
                replaced = replace_vowels(low)
                result = vowel_words.get(replaced, "")
            return result

        return [check(query) for query in queries]