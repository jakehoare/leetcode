_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shortest-word-distance-iii/
# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
# word1 and word2 may be the same and they represent two individual words in the list.

# As per problem 243 except if word1 == word2 treat indices as queue of length 2.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        last1, last2 = -1, -1   # last indices in words of word1 and word2
        same = word1 == word2   # only test once
        distance = len(words)

        for i, word in enumerate(words):
            if word == word1:
                if same:
                    last1, last2 = last2, i     # shift last2 to last1 and update last2 to i
                else:
                    last1 = i
            elif word == word2:
                last2 = i

            if last1 != -1 and last2 != -1:
                distance = min(distance, abs(last1 - last2))

        return distance