_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/uncrossed-lines/
# We write the integers of A and B (in the order they are given) on two separate horizontal lines.
# Now, we may draw a straight line connecting two numbers A[i] and B[j] as long as A[i] == B[j],
# and the line we draw does not intersect any other connecting (non-horizontal) line.
# Return the maximum number of connecting lines we can draw in this way.

# Dynamic programming. For each i element of the first list, find the maximum uncrossed lines we can draw for each
# element j of the second list.
# To get the result for i, j we can add 1 to the result for i - 1, j - 1 of the elements match, or ignore either i or j
# and take the result for i, j - 1 or i - 1, j.
# Time - O(mn)
# Space - O(min(m, n)

class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if len(A) < len(B):     # ensure B is shorter to use less space
            A, B = B, A
        max_uncrossed = [0] * (len(B) + 1)

        for i in range(len(A)):
            new_max_uncrossed = [0]
            for j in range(len(B)):
                new_max_uncrossed.append(max(max_uncrossed[j] + int(A[i] == B[j]),
                                             max_uncrossed[j + 1], new_max_uncrossed[-1]))
            max_uncrossed = new_max_uncrossed

        return max_uncrossed[-1]
