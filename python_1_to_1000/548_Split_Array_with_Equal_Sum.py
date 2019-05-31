_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/split-array-with-equal-sum/
# Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:
# 0 < i, i + 1 < j, j + 1 < k < n - 1
# Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.
# where we define that subarray (L, R) represents a slice of the original array starting from the element indexed L to
# the element indexed R

# For each possible middle index j, try all possible values of first index i and is this creates 2 equal subarrays then
# then add their sum to the candidates set. Then with the same value fo j, try all possible values of k. If the RHS
# subarrays have the same sum and that sum is in candidates the return True.
# Time - O(n**2)
# Space - O(n)

class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 7:
            return False

        cumul = [nums[0]]           # array of cumulative sums for easy lookup of subarray sums
        for num in nums[1:]:
            cumul.append(num + cumul[-1])

        for j in range(3, n - 3):   # possible value of middle index
            candidates = set()

            for i in range(1, j - 1):
                left_sum = cumul[i - 1]
                right_sum = cumul[j - 1] - cumul[i]
                if left_sum == right_sum:
                    candidates.add(left_sum)

            for k in range(j + 2, n - 1):
                left_sum = cumul[k - 1] - cumul[j]
                right_sum = cumul[n - 1] - cumul[k]
                if left_sum == right_sum and left_sum in candidates:
                    return True

        return False

