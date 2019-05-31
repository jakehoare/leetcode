_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/majority-element/
# Given an array of size n, find the majority element. The majority element appears more than [n/2] times.
# You may assume that the array is non-empty and the majority element always exist in the array.

# When the count is zero, the next element becomes the candidate. When an element is the same as the candidate,
# increment the count, else decrement the count.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, candidate = 0, None

        for i, num in enumerate(nums):

            if count == 0:
                candidate = num

            if candidate == num:
                count += 1
            else:
                count -= 1

        return candidate