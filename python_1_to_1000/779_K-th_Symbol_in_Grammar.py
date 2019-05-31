_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/k-th-symbol-in-grammar/
# On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each
# occurrence of 0 with 01, and each occurrence of 1 with 10.
# Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

# Each row consists of the concatenation of the previous row and the inverse of the previous row. If K is more than
# half way along a row, it belongs to the inverse of the previous row hence flip the logical flag. Repeat moving up
# rows until the final row is inversed (return 1) or not (return 0).
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        length = 2 ** (N - 1)           # length of current row

        inverse = False

        while length > 1:

            if K > length // 2:         # on RHS of this row
                inverse = not inverse
                K -= length // 2

            length //= 2

        return int(inverse)

