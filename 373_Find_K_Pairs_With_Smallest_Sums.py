_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
# Define a pair (u,v) which consists of one element from the first array and one element from the second array.
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

# Maintain a heap from which the smallest sums are removed.  Add the sum of elements at index 0 in both arrays to heap.
# Pop smallest from heap, add to heap the pair with incremented index from nums1 unless at end of nums1.  Add to heap
# the pair
# Time - O(k log k)
# Space - O(k)

import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []

        smallest = []
        frontier = [(nums1[0] + nums2[0], 0, 0)]

        while frontier and len(smallest) < k:
            _, i, j = heapq.heappop(frontier)
            smallest.append([nums1[i], nums2[j]])
            if len(frontier) >= k:      # limit heap size
                continue
            if i < len(nums1) - 1:      # not the last element of nums1
                heapq.heappush(frontier, (nums1[i + 1] + nums2[j], i + 1, j))
            if i == 0 and j < len(nums2) - 1:      # first element of nums 1 and not the last element of nums2
                heapq.heappush(frontier, (nums1[i] + nums2[j + 1], i, j + 1))

        return smallest