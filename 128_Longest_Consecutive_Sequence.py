_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-consecutive-sequence/
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# Test if each number starts a new sequence, if it does then count that sequence.
# Time - O(n), visits each number at most twice
# Space - O(n)

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set(nums)          # no ordering, O(1) lookup
        longest = 0

        for num in numset:

            if num-1 in numset:     # not the start of a sequence
                continue

            seq = 0
            while num in numset:    # move along this sequence
                seq += 1
                num += 1
            longest = max(longest, seq)

        return longest


