_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/set-mismatch/
# The set S originally contains numbers from 1 to n. But unfortunately, one of the numbers in the set got duplicated
# to another number in the set, which results in repetition of one number and loss of another number.
# Given an array nums representing the data status of this set after the error. Your task is to firstly find the
# number occurs twice and then find the number that is missing. Return them in the form of an array.

# Iterate over nums. When num is seen, set the num at index of abs(num) - 1 to negative. If the num at that index is
# already negative, it is the duplicate. Then find the index i that is not negative, which means i + 1 is missing.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            if nums[abs(num) - 1] < 0:
                duplicate = abs(num)
            else:
                nums[abs(num) - 1] *= -1

        for i, num in enumerate(nums):
            if num > 0:
                missing = i + 1
                break

        return [duplicate, missing]