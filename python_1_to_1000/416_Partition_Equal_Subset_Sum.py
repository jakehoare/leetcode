_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/partition-equal-subset-sum/
# Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets
# such that the sum of elements in both subsets is equal.

# Dynamic programming. Maintain array of which sums can be reached. Initially only zero. For each num starting with
# largest, add this to all xisting sums starting with largest existing.
# Alternatively, recursively use each remaining unique num and subtract from remaining target.
# Time - O(n * sum(nums))
# Space - O(sum(nums))

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False

        nums.sort(reverse = True)               # try largest nums first
        target = sum_nums // 2

        subset_sum = [True] + [False] * target

        for num in nums:
            for i in range(target - 1, -1, -1): # backwards so cannot use same num repeatedly
                if subset_sum[i] and i + num <= target:
                    if i + num == target:       # early return, solution found
                        return True
                    subset_sum[i + num] = True  # mark this value

        return False


from collections import Counter

class Solution2(object):
    def canPartition(self, nums):
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False

        freq = Counter(nums)
        return self.partition(freq, nums_sum // 2)

    def partition(self, freq, target):
        if target == 0:
            return True
        if target < 0:
            return False

        for num in freq:
            if freq[num] == 0:
                continue
            freq[num] -= 1      # remove from frequency count
            if self.partition(freq, target - num):
                return True
            freq[num] += 1      # add back to frequency count

        return False

