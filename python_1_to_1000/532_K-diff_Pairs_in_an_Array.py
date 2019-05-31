_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/k-diff-pairs-in-an-array/
# Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array.
# Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their
# absolute difference is k.

# Count the frequency of each num. If k is zero, count the duplicated nums. Else for each num, add to the result count
# if num + k is in nums.
# Time - O(n)
# Space - O(n)

from collections import Counter

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0

        freq = Counter(nums)
        pairs = 0

        for num in freq:
            if k == 0:
                if freq[num] > 1:
                    pairs += 1
            else:
                if num + k in freq:
                    pairs += 1

        return pairs