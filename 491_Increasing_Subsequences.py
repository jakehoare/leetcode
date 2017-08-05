_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/increasing-subsequences/
# Given an integer array, your task is to find all the different possible increasing subsequences of the given array,
# and the length of an increasing subsequence should be at least 2 .

# For each number, create a set of subsequences by extending all previous subsequences.
# Time - O(n**4), sum from i = 1 to n of i**3
# Space - O(n**3), n**2 subsequences of length n

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsequences = set()

        for num in nums:
            new_subsequences = set()
            new_subsequences.add((num,))
            for s in subsequences:
                if num >= s[-1]:
                    new_subsequences.add(s + (num,))    # tuple not list so can store in set

            subsequences |= new_subsequences

        return [s for s in subsequences if len(s) > 1]  # convert to list and filter out if too short