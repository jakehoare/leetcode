_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/pancake-sorting/
# Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length,
# then reverse the order of the first k elements of A.
# We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.
# Return the k-values corresponding to a sequence of pancake flips that sort A.
# Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

# For each number descending from the largest, find the index of the number. Flip the list up to and including that
# number to move it to the beginning. Then flip the list up to the end of the already sorted part, to add the
# number to the sorted part. The two flips combine to shift A[:i + 1] next to the already sort part and move the
# reversed A[i + 1:unsorted] to the beginning.
# Time - O(n**2)
# Space - O(n)

class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        flips = []

        for unsorted in range(len(A), 0, -1):       # each unsorted number in decresing order

            i = A.index(unsorted)
            if i == unsorted - 1:                   # already in correct position
                continue

            A = A[unsorted - 1:i:-1] + A[:i + 1] + A[unsorted:]
            flips += [i + 1, unsorted]

        return flips
