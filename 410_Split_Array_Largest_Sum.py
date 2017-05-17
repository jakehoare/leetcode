_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/split-array-largest-sum/
# Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty
# continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

# Binary search the range of possible smallest max subarray sums. If x is valid, search range x and below else search
# above x.
# Binary search must make progress each iteration. Since mid can equal left then next iteration brings right down to
# mid instead of left up (which may result in no change).  right = mid-1 and left=mid may not make progress.
# Time - O(n log sum(n))
# Space - O(1)

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        left, right = max(nums), sum(nums)  # search range

        while left < right:  # if left == right then return
            mid = (left + right) // 2
            if self.can_split(nums, m, mid):  # recurse on LHS (smaller max subarray sums) including mid
                right = mid     # mid < right so always make progress
            else:
                left = mid + 1

        return left

    def can_split(self, nums, m, max_subarray):  # can nums be split into m subarrays each sum <= max_subarray ?

        subarray_sum = 0
        for num in nums:
            if num + subarray_sum > max_subarray:  # num makes sum too big
                m -= 1  # one less subarray
                if m <= 0:  # at least num remain with no more subarrays to use
                    return False
                subarray_sum = num  # num in next subarray
            else:
                subarray_sum += num

        return True
