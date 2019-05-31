_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/delete-and-earn/
# Given an array nums of integers, you can perform operations on the array.
# In each operation, you pick any nums[i] and delete it to earn nums[i] points.
# After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.
# You start with 0 points. Return the maximum number of points you can earn by applying such operations.

# Create a sorted list of nums and their frequencies. Iterate over the list, calculating the max points if a num is
# used and the max if it is not used. If not previous num or previous is not num - 1 then we can choose the max of
# used and not_used for the new not_sed, addind the points from this num for the new used. If previous is num - 1
# then new used must be not_used + points from num. Again, not_sed chan chosse max of previous used and previous
# not_used.
# Time - O(n log n)
# Space - O(n)

from collections import Counter

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        pairs = [(num, count) for num, count in freq.items()]
        pairs.sort()

        used, not_used = 0, 0

        for i, (num, count) in enumerate(pairs):

            if i == 0 or pairs[i - 1][0] != num - 1:    # no previous noum or not num - 1
                not_used = max(used, not_used)          # choose max
                used = num * count + not_used           # add point from this num
            else:
                used, not_used = num * count + not_used, max(used, not_used)

        return max(used, not_used)
