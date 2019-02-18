_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/subarrays-with-k-different-integers/
# Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the
# number of different integers in that subarray is exactly K.
# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# Return the number of good subarrays of A.

# For each ending index of a subarray, find the starting index such that all subarrays contains at most K distinct
# elements. The difference between the at_most_k(K) and at_most_k(K - 1) is the number of subarrays with exactly K.
# A counter tracks the numbers in the sliding window, adding each element and decrementing the required distinct if
# the new element is not already in the window. Then while there are too many distinct elements, move the start index
# forward and remove elements from the window. Result is incremented by all subarrays of length <= end - start + 1.
# Time - O(n)
# Space - O(n)

from collections import Counter

class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        def at_most_k(distinct):

            count = Counter()
            subarrays = 0
            start = 0

            for end, num in enumerate(A):

                if count[num] == 0:
                    distinct -= 1
                count[num] += 1

                while distinct < 0:     # too many distinct elements
                    count[A[start]] -= 1
                    if count[A[start]] == 0:
                        distinct += 1
                    start += 1          # move start of window forwards

                subarrays += end - start + 1

            return subarrays

        return at_most_k(K) - at_most_k(K - 1)
