_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/permutations-ii/
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# Count occurences of each unique number.  Recursively append each number if still has a positive count.
# Time - O(n^2 * n!), as 046_Permutations if all numbers are unique
# Space - O(n * n!)

from collections import Counter

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        freq = Counter(nums)
        permutations = []
        self.permute_helper(len(nums), [], freq, permutations)
        return permutations

    def permute_helper(self, to_add, partial, freq, permutations):
        if to_add == 0:
            permutations.append(partial)

        for item in freq:
            if freq[item] > 0:
                freq[item] -= 1
                self.permute_helper(to_add-1, partial + [item], freq, permutations)
                freq[item] += 1

