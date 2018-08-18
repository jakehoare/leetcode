_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-mountain-in-array/
# Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:
# B.length >= 3
# There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
# (Note that B could be any subarray of A, including the entire array A.)
# Given an array A of integers, return the length of the longest mountain.
# Return 0 if there is no mountain.

# Iterate over A, comparing successive difference between points. Track the last valley where a mountain starts and
# the peak of the last mountain.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        valley, peak = 0, 0
        prev = 0                    # previous difference: 0 == same, +1 == up, -1 == down
        longest = 0

        for i in range(1, len(A)):

            if A[i] == A[i - 1]:    # if same, reset valley and peak to this index
                valley, peak = i, i
                prev = 0

            elif A[i] > A[i - 1]:
                if prev == 1:       # new peak
                    peak = i
                else:               # previous index was valley
                    valley = i - 1
                prev = 1

            elif A[i] < A[i - 1]:
                if prev == 1:       # previous index was peak
                    peak = i - 1
                    longest = max(longest, i - valley + 1)
                else:               # more recent peak than valley makes a mountain
                    if peak > valley:
                        longest = max(longest, i - valley + 1)
                prev = -1

        return longest