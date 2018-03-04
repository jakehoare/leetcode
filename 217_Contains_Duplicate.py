_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/contains-duplicate/
# Given an array of integers, find if the array contains any duplicates. Your function should return true if any value
# appears at least twice in the array, and it should return false if every element is distinct.

# If every number is unique then the set length is the same as the list length. If this is not true, then there is
# some duplicate.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)