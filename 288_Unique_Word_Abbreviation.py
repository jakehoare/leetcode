_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/unique-word-abbreviation/
# An abbreviation of a word follows the form <first letter><number><last letter>.
# Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary.
# A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

# Create a set of words form dictionary to eliminate duplicates so the same word is not double counted. For each
# unique word, create a mapping from its abbreviation to the count of words with the same abbreviation. A word is
# unique if it is in the dictionary and no other word has the same abbreviation, or no other word has same abbreviation.
# Time - O(n) for init() where n is the total number of letters in all words in the dictionary. O(k) for isUnique()
# where k is the length of the word to be tested for uniqueness.
# Space - O(n)

from collections import defaultdict

class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dictionary = set(dictionary)
        self.freq = defaultdict(int)
        for word in self.dictionary:
            self.freq[self.abbreviate(word)] += 1

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abbr = self.abbreviate(word)
        if word in self.dictionary:
            return self.freq[abbr] == 1
        else:
            return abbr not in self.freq

    def abbreviate(self, word):
        n = len(word)
        if n < 3:
            return word
        return word[0] + str(n - 2) + word[-1]