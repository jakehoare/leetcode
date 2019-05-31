_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/di-string-match/
# Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
# If S[i] == "I", then A[i] < A[i+1]
# If S[i] == "D", then A[i] > A[i+1]

# Iterate over S, tracking the next lowest and highest unused numbers.
# When the char is "I", append to the result the lowest unused number, since all future numbers are increasing.
# When the char is "D", append to the result the highest unused number, since all future numbers are decreasing.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        result = []
        low, high = 0, len(S)

        for c in S:

            if c == "I":
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1

        return result + [low]       # append the last unused number