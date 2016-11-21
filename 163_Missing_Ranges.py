_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/missing-ranges/
# Given a sorted integer array where elements are in the inclusive range [lower, upper], return its missing ranges.
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

# Track the last number seen.  If num == last_seen+2 then last_seen+1 is the start and end of a missing range.
# If num > last_seen+2 then inclusive range last_seen+1 to num-1 is missing.  Update last_seen.  Do nothing if
# num is last_seen or last_seen+1 since nothing is missing.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        last_seen = lower-1
        nums.append(upper+1)
        missing = []

        for num in nums:
            if num == last_seen + 2:
                missing.append(str(last_seen+1))
            elif num > last_seen + 2:
                missing.append(str(last_seen+1) + '->' + str(num-1))
            last_seen = num

        return missing
