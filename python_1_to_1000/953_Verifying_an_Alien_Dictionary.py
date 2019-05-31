_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/verifying-an-alien-dictionary/
# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
# The order of the alphabet is some permutation of lowercase letters.
# Given a sequence of words written in the alien language, and the order of the alphabet,
# return true if and only if the given words are sorted lexicographically in this alien language.

# Create a mapping from each char to its index in the alphabet. For each word, map each char to its index in the
# alphabet. Compare the mapped list lexicographically to the previous word's mapped list.
# Time - O(nk) for n words of maximum length k
# Space - O(k)

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        indices = {c: i for i, c in enumerate(order)}
        prev = []

        for word in words:
            mapping = [indices[c] for c in word]
            if mapping < prev:
                return False
            prev = mapping

        return True