_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/orderly-queue/
# A string S of lowercase letters is given. Then, we may make any number of moves.
# In each move, we choose one of the first K letters (starting from the left), remove it,
# and place it at the end of the string.
# Return the lexicographically smallest string we could have after any number of moves.

# If K == 1, we can cycle through the string appending any number of the first characters to the end. In this case, try
# all possible numbers of characters moved.
# Otherwise if K >= 2 then we can always swap the first 2 characters by moving the second before the first.
# Since we can perform any number of swaps, we
# Time - O(n**2)
# Space - O(n)

class Solution(object):
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if K > 1:
            return "".join(sorted(S))

        return min(S[i:] + S[:i] for i in range(len(S)))