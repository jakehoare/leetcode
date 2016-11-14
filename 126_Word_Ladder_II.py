_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/word-ladder-ii/
# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s)
# from beginWord to endWord, such that:
# Only one letter can be changed at a time and each intermediate word must exist in the word list

# Breadth first search.  Frontier of valid neighbouring words is gradually expanded.
# Time - O(b^d) where b is branching factor and d is depth between start and end

from collections import defaultdict
import string

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList.add(endWord)
        frontier = {beginWord}
        parents = defaultdict(set)

        while frontier and endWord not in parents:
            next_frontier = defaultdict(set)    # mapping of word to its parents

            for word in frontier:

                for char in string.ascii_lowercase:
                    for i in range(len(beginWord)):
                        next = word[:i] + char + word[i+1:]
                        if next in wordList and next not in parents:    # check parents if already seen this word
                            next_frontier[next].add(word)

            frontier = next_frontier
            parents.update(next_frontier)   # merge dictionaries

        ladders = [[endWord]]
        while ladders and ladders[0][0] != beginWord:   # build results with all parents
            ladders = [[p] + l for l in ladders for p in parents[l[0]]]
        return ladders

