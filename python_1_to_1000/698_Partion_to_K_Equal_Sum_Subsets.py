_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k
# non-empty subsets whose sums are all equal.

# Sort in decreasing order. Find some nums that sum to target, flagging each num in used. If a num is used then only
# search smaller nums since any larger would have been used already.
# Alternatively, add each number to each bucket with capacity and recurse, backtracking if a solution is not found.
# Time - O(k * 2**n) for k buckets, each number is or is not used in each
# Space - O(k * 2**n)

class Solution(object):
    def canPartitionKSubsets(self, nums, k):

        total = sum(nums)
        if total % k != 0:
            return False        # nums are not divisible equally

        target = total // k

        used = [False] * len(nums)

        nums.sort(reverse = True)
        if nums[0] > target:    # largest num too big
            return False

        def dfs(subsets, last, partial):

            if subsets == 1:    # base case, can always create one subset
                return True

            if partial == target:   # start a new subset
                return dfs(subsets - 1, 0, 0)

            for i in range(last, len(nums)):    # from last num onwards

                if not used[i] and partial + nums[i] <= target:
                    used[i] = True
                    if dfs(subsets, i + 1, partial + nums[i]):  # only search smaller nums
                        return True
                    used[i] = False

            return False

        return dfs(k, 0, 0)


class Solution2(object):
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        nums.sort(reverse = True)
        target = total // k
        if total % k != 0 or nums[0] > target:
            return False

        partition = [0 for _ in range(k)]

        def helper(i):                          # test whether nums[i] can be added to some partition
            if i == len(nums):
                return True

            for j in range(len(partition)):
                if partition[j] + nums[i] <= target:
                    partition[j] += nums[i]
                    if helper(i + 1):
                        return True
                    partition[j] -= nums[i]
                if partition[j] == 0:           # do not try other empty buckets
                    break

            return False

        return helper(0)