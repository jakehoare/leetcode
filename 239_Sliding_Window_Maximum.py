_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sliding-window-maximum/
# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the
# very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return a list of the max number in each window of the sliding window.

# Keep indices in double ended queue.  New indices are added at head of queue (RHS) so oldest are at tail (LHS).
# Before adding a new index, pop from tail all indexes whose numbers are less than the new num since they can
# never be the window max.  Pop from head if that index is now outside the window.  Head has largest in window.
# Time - O(n)
# Space - O(k)

from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = deque()
        max_window = []

        for i, num in enumerate(nums):

            while q and nums[q[-1]] < num:  # pop smaller numbers from RHS
                q.pop()

            q.append(i)         # append this number at RHS

            if q[0] <= i - k:   # if LHS is outside window, remove it
                q.popleft()

            if i >= k - 1:      # if window is at least k, add LHS to result
                max_window.append(nums[q[0]])

        return max_window