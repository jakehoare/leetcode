_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/add-and-search-word-data-structure-design/
# Design a data structure that supports the following two operations:
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or '.' (one letter).

# Store of a list of words by length.  Check search word against list of words of same length by checking each char
# and ignoring '.'.
# Alternatively use a trie to store words and when search char is '.' then search all children.
# Time - O(1) to addWord, O(n * k_ search where there are n strings of length k
# Space - O(t), total number of chars in all strings

from collections import defaultdict

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.words = defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.words[len(word)].append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        for w in self.words[len(word)]:
            for i, c in enumerate(w):
                if word[i] != '.' and word[i] != c:
                    break
            else:
                return True
        return False

