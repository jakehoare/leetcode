_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/delete-columns-to-make-sorted-iii/
# We are given an array A of N lowercase letter strings, all of the same length.
# Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.
# For example, if we have an array A = ["babca","bbazb"] and deletion indices {0, 1, 4},
# then the final array after deletions is ["bc","az"].
# Suppose we chose a set of deletion indices D such that after deletions, the final array has every element (row)
# in lexicographic order.
# For clarity, A[0] is in lexicographic order (ie. A[0][0] <= A[0][1] <= ... <= A[0][A[0].length - 1]), A[1] is in
# lexicographic order (ie. A[1][0] <= A[1][1] <= ... <= A[1][A[1].length - 1]), and so on.
# Return the minimum possible value of D.length.

# Find the maximum length subsequence containing columns which are already sorted.
# Dynamic programming recording the max_subsequence ending at each index.
# For each ending index, for each other index, update the max_subsequence if the ending and other columns are sorted.
# Update is the max of current max_subsequence and 1 + max_subsequence ending at other index.
# Time - O(n**2 m)
# Space - O(n)

class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        rows, cols = len(A), len(A[0])
        max_subsequence = [1] * cols

        for col_end in range(1, cols):
            for col in range(col_end):
                if all(A[r][col] <= A[r][col_end] for r in range(rows)):
                    max_subsequence[col_end] = max(max_subsequence[col_end],
                                                   max_subsequence[col] + 1)

        return cols - max(max_subsequence)
