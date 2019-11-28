_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/greatest-sum-divisible-by-three/
# Given an array nums of integers,
# we need to find the maximum possible sum of elements of the array such that it is divisible by three.

# If the sum of elements is divisible by 3, return that sum.
# Else make sorted lists of the elements divisible by 1 and 2.
# If the remainder of the sum after dividing by 3 is 1, we can subtract the smallest element divisible by 1,
# or subtract the 2 smallest elements divisible by 2.
# If the remainder of the sum after dividing by 3 is 2, we can subtract the smallest element divisible by 2,
# or subtract the 2 smallest elements divisible by 1.
# Return the maximum candidate.
# Time - O(n log n)
# Space - O(n)

class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        rem = total % 3

        if rem == 0:
            return total

        rem_1 = [num for num in nums if num % 3 == 1]
        rem_2 = [num for num in nums if num % 3 == 2]
        rem_1.sort()
        rem_2.sort()

        candidates = [0]        # default 0
        if rem == 1:
            if rem_1:
                candidates.append(total - rem_1[0])
            if len(rem_2) >= 2:
                candidates.append(total - sum(rem_2[:2]))
        elif rem == 2:
            if rem_2:
                candidates.append(total - rem_2[0])
            if len(rem_1) >= 2:
                candidates.append(total - sum(rem_1[:2]))

        return max(candidates)
