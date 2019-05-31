_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/word-ladder-ii/
# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s)
# from beginWord to endWord, such that:
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

# Bidirectional breadth first search. Frontiers of valid neighbouring words are gradually expanded. Swap to use the
# smaller frontier in each round, stop when either frontier is empty (return empty list) or an intersection is found.
# Build ladders to srat using left parents and to end using right parents.
# Time - O(b^(d/2)) where b is branching factor and d is depth between start and end

from collections import defaultdict
import string

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []

        wordList = set(wordList)                    # convert to set for O(1) lookup
        left, right = {beginWord}, {endWord}        # frontiers at both ends
        left_parents, right_parents = defaultdict(set), defaultdict(set)    # map word to its parent
        swapped = False                             # have the frontiers been swapped?

        while left and right and not (left & right):    # while both frontiers and no intersection

            if len(right) < len(left):              # swap to expand smaller frontier
                left, right = right, left
                left_parents, right_parents = right_parents, left_parents
                swapped = not swapped

            next_left = defaultdict(set)
            for word in left:
                for char in string.ascii_lowercase:
                    for i in range(len(beginWord)):
                        n = word[:i] + char + word[i + 1:]  # replace every position with every char
                        if n in wordList and n not in left_parents: # valid word not been used
                            next_left[n].add(word)

            left_parents.update(next_left)
            left = set(next_left.keys())

        if swapped:                                 # swap back
            left, right = right, left
            left_parents, right_parents = right_parents, left_parents

        ladders = [[word] for word in left & right] # start from central intersection
        while ladders and ladders[0][0] not in beginWord:   # extend ladders left to start
            ladders = [[p] + l for l in ladders for p in left_parents[l[0]]]
        while ladders and ladders[0][-1] != endWord:        # extend ladders right to end
            ladders = [l + [p] for l in ladders for p in right_parents[l[-1]]]

        return ladders