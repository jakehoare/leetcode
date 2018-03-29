_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shortest-word-distance/
# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

# Iterate over list, updating the last seen indices whenever word matches word1 or word2. Also update the shortest
# distance.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        shortest = len(words)
        i_1, i_2 = float("-inf"), float("-inf")         # last seen indices of word1 and word2

        for i, word in enumerate(words):

            if word == word1:
                i_1 = i
                shortest = min(shortest, i_1 - i_2)
            if word == word2:
                i_2 = i
                shortest = min(shortest, i_2 - i_1)

        return shortest