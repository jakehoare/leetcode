_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/short-encoding-of-words/
# Given a list of words, we may encode it by writing a reference string S and a list of indexes A.
# For example, we can write words ["time", "me", "bell"], as S = "time#bell#" and indexes = [0, 2, 5].
# Then for each index, we will recover the word by reading from the reference string from that index until we
# reach a "#" character.
# What is the length of the shortest reference string S possible that encodes the given words?

# Create the set of required words, initially as all words without duplicates. For each word, remove all suffixes
# fromt the required set. Sum the lengths of all remaining words + 1 char per word for the sentinel "#".
# Time - O(nk) for n words of maximum length k
# Space - O(nk)

class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        required = set(words)

        for word in words:                          # iterate over list, not the required set
            for i in range(1, len(word) - 1):       # remove from required any suffix of word
                required.discard(word[i:])          # discard() not remove()

        return sum(len(w) for w in required) + len(required)