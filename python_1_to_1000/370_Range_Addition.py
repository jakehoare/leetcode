_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/range-addition/
# Assume you have an array of length n initialized with all 0's and are given k update operations.
# Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of
# subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.
# Return the modified array after all k operations were executed.

# To a list of length length + 1, add increments at starting index of each update and decrements after ending index.
# Iterate over shifts, creating a cumulative sum.
# Time - O(n + k) where n = length and k = len(updates)
# Space - O(n)

class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        if length <= 0:
            return []

        shifts = [0] * (length + 1)
        for start, end, inc in updates:
            shifts[start] += inc
            shifts[end + 1] -= inc

        output = [shifts[0]]
        for i in range(1, length):
            output.append(output[-1] + shifts[i])

        return output