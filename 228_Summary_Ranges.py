_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/summary-ranges/
# Given a sorted integer array without duplicates, return the summary of its ranges.
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

# Create a list of pair [start, end] for each range.  Extend previous range if new num is previous + 1, else
# start a new range.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        summary = []
        for num in nums:
            if not summary or num > summary[-1][1] + 1:
                summary.append([num, num])
            else:
                summary[-1][1] = num

        result = [str(i) if i == j else str(i) + '->' + str(j) for i, j in summary]
        return result