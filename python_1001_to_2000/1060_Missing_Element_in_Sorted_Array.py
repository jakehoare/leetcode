_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/missing-element-in-sorted-array/
# Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

# Iterate along nums, subtracting the number of missing elements from k until no more missing elements are required.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.append(float("inf"))       # add infinity so we check after the final element of nums
        prev = nums[0]

        for num in nums[1:]:
            missing = num - prev - 1    # count of missing elements between num and prec
            if k - missing <= 0:        # missing element is between num and prev
                return prev + k
            k -= missing
            prev = num
