_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/subsets/
# Given a set of distinct integers, nums, return all possible subsets.
# The solution set must not contain duplicate subsets.

# Each bit of binary number form 0 to 2**n - 1 represents whether or not an entry in nums is in that set.
# Alternatively, copy partial subsets both with and without each item.
# Time - O(n * 2**n), 2**n subsets each of length n.
# Space - O(n * 2**n)

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nb_subsets = 2**len(nums)
        all_subsets = []

        for subset_nb in range(nb_subsets):

            subset = []
            for num in nums:
                if subset_nb % 2 == 1:
                    subset.append(num)
                subset_nb //= 2

            all_subsets.append(subset)

        return all_subsets
