_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/max-consecutive-ones-ii/
# Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

# Record the start of the current sequence and the start of the previous sequence (flipping a zero).
# Iterate over array, incrementing sequence end. If two zeros, reset prev_start to current. If single zero, update max
# and prev_start to start.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_consecutive = 0
        i = 0
        while i < len(nums) and nums[i] == 0:   # find first one
            i += 1
        start, prev_start = i, max(i - 1, 0)

        for j in range(i + 1, len(nums)):

            if nums[j] == 0:
                if j != 0 and nums[j - 1] == 0:
                    prev_start = j      # prefix new sequence by 1
                else:
                    max_consecutive = max(max_consecutive, j - prev_start)
                    prev_start = start  # use 1 to fill gap

                start = j + 1           # start new sequence at next index

        return max(max_consecutive, len(nums) - prev_start)     # cover case of final sequence
