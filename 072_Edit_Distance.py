_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/edit-distance/
# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.
# You have the following 3 operations permitted on a word (each 1 step):
# a) Insert a character
# b) Delete a character
# c) Replace a character

# Dynamic programming. Base case if either string is empty, return unmatched length of other string.
# If last characters matched then same cost as matching other characters.  Else best case of insert, delete or replace.
# Time - O(m * n)
# Space - O(m * n)

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return self.edit_distance(word1, len(word1)-1, word2, len(word2)-1, {})

    def edit_distance(self, word1, i, word2, j, memo):      # i, j are next indices to be matched
        if i < 0 or j < 0:
            return i + 1 + j + 1

        if (i, j) in memo:
            return memo[(i, j)]

        if word1[i] == word2[j]:
            result = self.edit_distance(word1, i-1, word2, j-1, memo)
        else:
            result = 1 + min(self.edit_distance(word1, i-1, word2, j, memo),
                             self.edit_distance(word1, i, word2, j-1, memo),
                             self.edit_distance(word1, i-1, word2, j-1, memo))

        memo[(i, j)] = result
        return result
