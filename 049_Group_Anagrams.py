_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/anagrams/
# Given an array of strings, group anagrams together.

# Sort the letters in each word.  Use sorted words as dictionary keys, values are unsorted words.
# Anagrams have equivalent sorted words.
# Time - O(k log k * n) for n words of length k
# Space - O(k * n)

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_words = defaultdict(list)

        for word in strs:
            letter_list = [c for c in word]
            letter_list.sort()
            sorted_word = "".join(letter_list)
            sorted_words[sorted_word].append(word)

        return list(sorted_words.values())