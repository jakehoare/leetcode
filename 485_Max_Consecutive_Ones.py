_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/max-consecutive-ones/
# Given a binary array, find the maximum number of consecutive 1s in this array.

# Iterate over nums. If we see a zero, update max_consecutive and reset consecutive. If we see a one, increment
# consecutive.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        consecutive, max_consecutive = 0, 0

        for num in nums:
            if num == 0:
                max_consecutive = max(max_consecutive, consecutive)
                consecutive = 0
            else:
                consecutive += 1

        return max(max_consecutive, consecutive)    # check final sequence
