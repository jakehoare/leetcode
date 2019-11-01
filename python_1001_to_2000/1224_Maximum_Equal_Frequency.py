_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-equal-frequency/
# Given an array nums of positive integers, return the longest possible length of an array prefix of nums,
# such that it is possible to remove exactly one element from this prefix so that every number that has
# appeared in it will have the same number of occurrences.
# If after removing one element there are no remaining elements,
# it's still considered that every appeared number has the same number of ocurrences (0).

# Iterate over nums, counting the occurrences of each num amd tracking the maximum count of any num.
# Also maintain a mapping from the count of a num to the number of different nums with that count.
# If the maximum count is 1, we can remove any num and all others appear once.
# If all numbers apart from one have have a count of max_count - 1, we can remove one of the number with max_count and
# then all numbers appear max_count - 1 times.
# If all numbers apart from one have have a count of max_count and the pther number has a count of 1, we can remove
# the other number so all have counts of max_count.
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_to_count, count_of_counts = defaultdict(int), defaultdict(int)

        result = 0
        max_count = 0

        for i, num in enumerate(nums):
            count = num_to_count[num] + 1
            num_to_count[num] = count
            max_count = max(max_count, count)

            if count != 1:
                count_of_counts[count - 1] -= 1     # remove previous count_of_counts
            count_of_counts[count] += 1

            if max_count == 1:
                result = i + 1
            elif count_of_counts[max_count - 1] == len(num_to_count) - 1:
                result = i + 1
            elif count_of_counts[max_count] == len(num_to_count) - 1 and count_of_counts[1] == 1:
                result = i + 1

        return result
