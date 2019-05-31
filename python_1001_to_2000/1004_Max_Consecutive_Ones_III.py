_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/max-consecutive-ones-iii/
# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
# Return the length of the longest (contiguous) subarray that contains only 1s.

# Maintain a sliding window of length the maximum contiguous subarray. Iterate over A. If we have a zero, decrement
# the balance of additional ones we can add. If the balance becomes negative, we have used too many ones so move the
# start of the window forward, which increases the balance of additional ones if the element at the start of window
# was zero.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        i = 0       # index of start of window

        for j in range(len(A)):     # index of end of window

            K -= 1 - A[j]
            if K < 0:   # length of window only increases if K >= 0
                K += 1 - A[i]
                i += 1

        return len(A) - i
