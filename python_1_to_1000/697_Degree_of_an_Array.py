_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/degree-of-an-array/
# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency
# of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray of nums that has the same degree as nums.

# Count the frequency of each num and record its first and last index. Then find the num or nums with the largest count.
# Finally, find the shortest distance between first and last indices of each maximum count num.
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts, limits = defaultdict(int), {}

        for i, num in enumerate(nums):

            counts[num] += 1

            if num not in limits:
                limits[num] = [i, i]    # first and last indices are both i
            else:
                limits[num][-1] = i     # new last index of i

        max_count, max_nums = 0, []     # list of nums with max_count
        for num, count in counts.items():

            if count == max_count:
                max_nums.append(num)    # new num with same max_count
            elif count > max_count:
                max_nums = [num]        # new unique max
                max_count = count

        shortest = float("inf")
        for num in max_nums:
            shortest = min(shortest, limits[num][1] - limits[num][0] + 1)

        return shortest