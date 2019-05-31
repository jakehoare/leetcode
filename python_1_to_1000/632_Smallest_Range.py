_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/smallest-range/
# You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one
# number from each of the k lists.
# We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

# Maintain a priority queue 'window' with one number from each list, initially the first. Remove lowest num from
# window and add next num from its list. Update the heap min and max, and potentially overall min and max.
# Time - O(m log n) where m is the total number of nums and n is number of lists
# Space - O(n)

import heapq

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)                                       # number of lists
        window = [(nums[i][0], 0, i) for i in range(n)]     # (num, index in list, index of list)
        heapq.heapify(window)
        heap_min, heap_max = window[0][0], max([nums[i][0] for i in range(n)])
        best_min, best_max = heap_min, heap_max

        while True:
            _, i, i_list = heapq.heappop(window)           # remove smalles num from window

            if i + 1 >= len(nums[i_list]):                  # end of i_list
                return [best_min, best_max]

            heapq.heappush(window, (nums[i_list][i + 1], i + 1, i_list))    # push next num from i_list
            heap_min = window[0][0]
            heap_max = max(heap_max, nums[i_list][i + 1])
            if heap_max - heap_min < best_max - best_min:   # keep current range if not better
                best_min, best_max = heap_min, heap_max