_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-harmonious-subsequence/
# We define a harmonious array is an array where the difference between its maximum value and its minimum value
# is exactly 1. Given an integer array, you need to find the length of its longest harmonious subsequence among all
# its possible subsequences.

# Count the frequency of each num in nums. For each num we create a subsequence of that num and num + 1. If num + 1 is
# not in nums then no subsequence can be created. Else update max_harmonious according to counts of num and num + 1.
# Time - O(n)
# Space - O(n)

from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        max_harmonious = 0

        for num, count in freq.items():
            if num + 1 in freq:         # difference must be exactly one, not zero
                max_harmonious = max(max_harmonious, count + freq[num + 1])

        return max_harmonious
