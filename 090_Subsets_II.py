_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/subsets-ii/
# Given a collection of integers that might contain duplicates, nums, return all possible subsets.
# Note: The solution set must not contain duplicate subsets.

# Count the frequency of times each num in nums.  Starting with the empty subset, for each num append it to all
# subsets every possible number of times (between 0 and its frequency in nums, inclusive).
# Time - O(n * 2**n), worst case when nums are all ujnique
# Space - O(n * 2**n)

from collections import Counter

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num_count = Counter(nums)
        results = [[]]

        for num in num_count:
            results += [partial+[num]*i for i in range(1,num_count[num]+1) for partial in results]

        return results

