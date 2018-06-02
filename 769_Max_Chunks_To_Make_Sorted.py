_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/max-chunks-to-make-sorted/
# Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of
# "chunks" (partitions), and individually sort each chunk. After concatenating them, the result equals the sorted array.
# What is the most number of chunks we could have made?

# Iterate from right to left, finding the minimum value to the right of each number. Then iterate from left to right
# tracking the maximum number in each partition. If the maximum is smaller than all numbers to the right, the partition
# can be sorted and the whole list will be sorted.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        min_right = [float("inf") for _ in range(len(arr))]     # min_right[-1] == float("inf")

        for i in range(len(arr) - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], arr[i + 1])

        partitions = 0
        partition_max = None

        for i, num in enumerate(arr):

            partition_max = num if partition_max is None else max(partition_max, num)

            if partition_max < min_right[i]:
                partitions += 1
                partition_max = None

        return partitions