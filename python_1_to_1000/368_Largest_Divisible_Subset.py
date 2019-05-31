_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/largest-divisible-subset/
# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this
# subset satisfies: Si % Sj = 0 or Sj % Si = 0.  If there are multiple solutions, return any subset.

# For each num starting with smallest, create a set where every pair is divisible.  Search through all existing sets
# to find the largest where num is divisible by its largest element (therefore num is divisible by all of its elements)
# Time - O(n**2)
# Space - O(n)

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        max_to_set = {-1 : set()}   # mapping from largest value in a set to its elements
        nums.sort()

        for num in nums:

            num_set = set()         # the set that has num as its largest value
            for max_in_s, s in max_to_set.items():
                if num % max_in_s == 0 and len(s) > len(num_set):
                    num_set = s

            max_to_set[num] = num_set | {num}   # include num in the set

        return list(max(max_to_set.values(), key = len))    # max set by length