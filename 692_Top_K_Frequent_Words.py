_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/top-k-frequent-words/
# Given a non-empty list of words, return the k most frequent elements.
# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the
# word with the lower alphabetical order comes first.

# Count the frequencies and heapify tuples of (-count, word). The pop the first k entries from the heap.
# Time - O(n + k log n) since O(n) to count and heapify, then O(log N) for each of the k pops
# Space - O(N)

from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq = Counter(words)
        pairs = [(-count, word) for word, count in freq.items()]
        heapq.heapify(pairs)
        return [heapq.heappop(pairs)[1] for _ in range(k)]