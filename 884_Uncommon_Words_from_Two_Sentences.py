_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/uncommon-words-from-two-sentences/
# We are given two sentences A and B. A sentence is a string of space separated words.
# Each word consists only of lowercase letters.
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
# Return a list of all uncommon words in any order.

# Add the counts of frequencies of words in each sentence. Return the list of words whose total count is one.
# Time - O(m + n)
# Space - O(m + n)

from collections import Counter

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        counts = Counter(A.split(" ")) + Counter(B.split(" "))
        return [word for word, count in counts.items() if count == 1]