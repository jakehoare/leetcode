_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/array-nesting/
# A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S,
# where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.
# Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should
# be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.

# Each set forms an independent cycle of nums. For each num, follow the cycle until a num repeats. Update the longest
# and add all nus in the cycle to the seen set. Iterate over nums finding the cycle for each num, ignoring any num
# already known to be part of a cycle.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = set()             # nums visited
        longest = 0                 # biggest set

        for i, num in enumerate(nums):

            if num in visited:
                continue

            current = set()         # start a new set
            while num not in current:
                current.add(num)    # add num
                num = nums[num]     # move to next num

            longest = max(longest, len(current))
            if longest >= len(nums) - i - 1:    # early return
                break

            visited |= current      # add all of current to visited

        return longest
