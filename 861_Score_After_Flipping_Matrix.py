_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/score-after-flipping-matrix/
# We have a two dimensional matrix A where each value is 0 or 1.
# A move consists of choosing any row or column, and toggling each value in that row or column:
# changing all 0s to 1s, and all 1s to 0s.
# After making any number of moves, every row of this matrix is interpreted as a binary number,
# and the score of the matrix is the sum of these numbers.
# Return the highest possible score.

# Return False if lengths are not equal. If strings are the same then return True if any letter is duplicated in A,
# else return False. Otherwise find the indices in A of letters that are in the wrong place. If there are not 2 such
# indices, return False. Finally, check if swapping the letters in the out of place positions will change A into B.
# Time - O(n)
# Space - O(n)

from collections import Counter

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False

        if A == B:
            return any(count > 1 for count in Counter(A).values())

        diffs = [i for i in range(len(A)) if A[i] != B[i]]      # indices of letters out of place in A
        if len(diffs) != 2:
            return False
        return A[diffs[0]] == B[diffs[1]] and A[diffs[1]] == B[diffs[0]] # swapping letters at misplaced indices