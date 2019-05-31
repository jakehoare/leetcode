_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/top-k-frequent-elements/
# Given a non-empty array of integers, return the k most frequent elements.

# Count the frequency of each element. Bucket sort the elements by frequency since the highest frequency cannot be
# more than the length of nums. Take the most frequent buckets, ties are split randomly.
# Time - O(n)
# Space - O(n)

from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        frequencies = [[] for _ in range(n + 1)]

        for num, freq in Counter(nums).items():
            frequencies[freq].append(num)

        top_k = []
        while k:
            while not frequencies[n]:
                n -= 1
            top_k.append(frequencies[n].pop())
            k -= 1

        return top_k