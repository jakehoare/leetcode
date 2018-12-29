_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/delete-columns-to-make-sorted-ii/
# We are given an array A of N lowercase letter strings, all of the same length.
# Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.
# For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after
# deletions is ["bef","vyz"].
# Suppose we chose a set of deletion indices D such that after deletions,
# the final array has its elements in lexicographic order (A[0] <= A[1] <= A[2] ... <= A[A.length - 1]).
# Return the minimum possible value of D.length.

# Iterate over columns, tracking which rows must be checked (i.e. are not known to be sorted).
# For each column, compare the char at each row to be checked against the previous row. If any char is not sorted, the
# column must be deleted. Chars that are in the correct order are flagged so as not to be tested again, unless the
# column is deleted. Identical chars are left to be checked in the next column.
# Time - O(mn)
# Space - O(m), number of rows

class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        rows, cols = len(A), len(A[0])
        cols_deleted = 0
        rows_to_check = {row for row in range(1, rows)}     # all rows apart from first

        for col in range(cols):

            new_checks = set(rows_to_check)
            for row in rows_to_check:

                char = A[row][col]
                prev_char = A[row - 1][col]

                if char < prev_char:                        # incorrect order
                    cols_deleted += 1
                    break
                elif char > prev_char:                      # correct order, do not check again
                    new_checks.remove(row)

            else:                                           # col not deleted
                if not new_checks:                          # finished
                    break
                rows_to_check = new_checks                  # update rows_to_check

        return cols_deleted
