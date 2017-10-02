_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/median-of-two-sorted-arrays/
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Find the middle element if sum of input list lengths is odd, or else the average of the middle pair.
# get_kth_smallest recusively removes k//2 elements from one list.
# Time - O(log(m+n)), half of the elements smaller than median are removed each recursive call.
# Space - O(log(m+n)) for the recursive call stack.

class Solution(object):

    def findMedianSortedArrays(self, A, B):

        right = self.get_kth_smallest(A, 0, B, 0, 1 + (len(A) + len(B))//2)
        if (len(A) + len(B)) % 2 == 1:      # odd total length
            return right

        left = self.get_kth_smallest(A, 0, B, 0, (len(A) + len(B))//2)
        return (left + right) / 2.0


    def get_kth_smallest(self, A, a_start, B, b_start, k):

        if k <= 0 or k > len(A) - a_start + len(B) - b_start:
            raise ValueError('k is out of the bounds of the input lists')

        # base cases
        if a_start >= len(A):
            return B[b_start + k - 1]
        if b_start >= len(B):
            return A[a_start + k - 1]
        if k == 1:
            return min(A[a_start], B[b_start])

        # remove k//2 elements from one list
        # find the smallest of the k//2 - 1th element from both lists and recurse having reduced that list.
        # k//2 - 1th element must exist in at least 1 list
        mid_A, mid_B = float('inf'), float('inf')
        if k//2 - 1 < len(A) - a_start:
            mid_A = A[a_start + k//2 - 1]
        if k//2 - 1 < len(B) - b_start:
            mid_B = B[b_start + k//2 - 1]

        if mid_A < mid_B:
            return self.get_kth_smallest(A, a_start + k//2, B, b_start, k - k//2)
        return self.get_kth_smallest(A, a_start, B, b_start + k//2, k - k//2)
