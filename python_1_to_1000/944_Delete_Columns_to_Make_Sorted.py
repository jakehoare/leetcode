_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/delete-columns-to-make-sorted/
# We are given an array A of N lowercase letter strings, all of the same length.
# Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.
# For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3},
# then the final array after deletions is ["bef", "vyz"],
# and the remaining columns of A are ["b","v"], ["e","y"], and ["f","z"].
# Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]].
# Suppose we chose a set of deletion indices D such that after deletions,
# each remaining column in A is in non-decreasing sorted order.
# Return the minimum possible value of D.length.

# Rotate the array to iterate over columns. Check if each column is sorted.
# Time - O(m n log n)
# Space - O(mn)

class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        deletions = 0

        for col in zip(*A):     # pass each string as a positional argument to zip

            if list(col) != sorted(col):
                deletions += 1

        return deletions