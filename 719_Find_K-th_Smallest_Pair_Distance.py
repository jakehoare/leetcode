_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-k-th-smallest-pair-distance/
# Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is
# defined as the absolute difference between A and B.

# Sort nums. Binary search for the smallest difference that has at least k pairs. For mid difference, check if
# k or more piars have that difference. If so, reduce hihg to mid, else increase low to mid + 1.
# Count number of differences <= diff by iterating over nums and for each num finding the first other num <= diff.
# Time - O(n log n)
# Space - O(n)

class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def k_pair_distances(diff):
            count, j = 0, 0
            for i, num in enumerate(nums):      # each starting num
                while num - nums[j] > diff:     # increase j until distance <= diff
                    j += 1
                count += i - j                  # add all pairs
            return count >= k

        nums.sort()
        left, right = 0, nums[-1] - nums[0]

        while left < right:

            mid = (left + right) // 2

            if k_pair_distances(mid):   # at least k pairs with difference of mid, search mid and lower
                right = mid
            else:
                left = mid + 1          # less than k pairs with distance mid, search above mid

        return left

