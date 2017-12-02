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

        def edit_distance(i, j):
            if i < 0 or j < 0:
                return i + 1 + j + 1

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                result = edit_distance(i - 1, j - 1)
            else:
                result = 1 + min(edit_distance(i - 1, j),
                                 edit_distance(i, j - 1),
                                 edit_distance(i - 1, j - 1))

            memo[(i, j)] = result
            return result

        memo = {}
        return edit_distance(len(word1) - 1, len(word2) - 1)
