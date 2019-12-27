_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
# Given an array of integers nums and a positive integer k,
# find whether it's possible to divide this array into sets of k consecutive numbers
# Return True if its possible otherwise return False.

# Count each num.
# Find the count of each num in sorted order,
# and check if there are at least as many of each k - 1 subsequent digits.
# Time - O(n log n)
# Space - O(n)

from collections import Counter

class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) % k != 0:  # check if nums can be divided into groups of k
            return False

        counts = Counter(nums)

        for start_num in sorted(counts.keys()):
            count = counts[start_num]
            if count == 0:              # num has already been used in other sequences
                continue

            for num in range(start_num, start_num + k):
                if num not in counts or counts[num] < count:
                    return False
                counts[num] -= count    # decrement so count nums are not reused

        return True
