_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-product-of-word-lengths/
# Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not
# share common letters. You may assume that each word will contain only lower case letters.
# If no such two words exist, return 0.

# Encode each word as an integer (up to (2^26)-1) with each set bit indicating the presence of a letter.  Check all
# pairs of codes, if the logical AND of the codes is zero then they have no letters in common.
# Alternatively sort worst in decreasing length order and break code comparison when max_product can no longer be
# exceeded.
# Time - O(n**2)
# Space - O(n)

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        codes = []              # set a bit for each letter present in word
        for word in words:
            codes.append(sum(1 << (ord(c) - ord('a')) for c in set(word)))

        max_product = 0
        for i in range(len(codes)-1):
            for j in range(i+1, len(codes)):
                if not (codes[i] & codes[j]):
                    max_product = max(max_product, len(words[i]) * len(words[j]))
        return max_product