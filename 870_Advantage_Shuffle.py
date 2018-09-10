_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/advantage-shuffle/
# Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i
# for which A[i] > B[i].
# Return any permutation of A that maximizes its advantage with respect to B.

# Sort B, storing the index of each element along with its value. For each element a of sorted(A), if a > smallest
# unused element of B then put a in the result at the index of the smallest unused element of B. Else a is not
# greater than any element of B, so put it in the result at the largest unused element of B.
# Time - O(n log n)
# Space - O(n)

class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        B_i = sorted([(b, i) for i, b in enumerate(B)])
        result = [None] * len(A)
        i = 0

        for a in sorted(A):

            if a > B_i[i][0]:
                result[B_i[i][1]] = a
                i += 1
            else:
                result[B_i.pop()[1]] = a

        return result