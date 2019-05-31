_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-longest-increasing-subsequence/
# Given an unsorted array of integers, find the number of longest increasing subsequence.

# For each num, find the longest increasing subsequence of the array up to and including that num, and the count of
# such longest subsequences. Fro each num, consider all previous nums that are lower. If we can make a new longest
# subsequence then we can extend every longest subsequence ending at the previous num. If we can make the same longest
# subsequence then we can add every longest subsequence ending at the previous num to the count.
# Time - O(n**2)
# Space - O(n)

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        lengths, counts = [], []

        for i, num in enumerate(nums):

            length, count = 1, 1    # default if num does not increase any subsequence

            for j in range(i):
                if num > nums[j]:                   # num can extend sequence
                    if lengths[j] + 1 > length:     # new best length
                        length = lengths[j] + 1
                        count = counts[j]
                    elif lengths[j] + 1 == length:  # same best length
                        count += counts[j]          # add to count of best length

            lengths.append(length)
            counts.append(count)

        longest = max(lengths)
        return sum([count for length, count in zip(lengths, counts) if length == longest])
