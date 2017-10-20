_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shortest-word-distance-ii/
# Design a class which receives a list of words in the constructor, and implements a method that takes two words word1
# and word2 and return the shortest distance between these two words in the list. Distance is the difference between
# the indices of the words in the list.
# Your method will be called repeatedly many times with different parameters.

# Dictionary stores and ordered list of the indices of each word in words.
# Iterate along the lists of indices of each word together, moving forwards the pointer to the lower index.
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.word_indices = defaultdict(list)
        for i, word in enumerate(words):
            self.word_indices[word].append(i)

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1 = self.word_indices[word1]   # list of indices of word1
        i2 = self.word_indices[word2]   # list of indices of word2
        distance = float('inf')
        p1, p2 = 0, 0                   # pointers to indices in the lists

        while p1 < len(i1) and p2 < len(i2):    # break when either pointer exceeds its list

            distance = min(distance, abs(i1[p1] - i2[p2]))
            if i1[p1] < i2[p2]:     # index of word1 is less than index of word2
                p1 += 1
            else:
                p2 += 1

        return distance
