_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/first-bad-version/
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version
# of your product fails the quality check. Since each version is developed based on the previous version, all the
# versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the
# following ones to be bad.
# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to
# find the first bad version. You should minimize the number of calls to the API.

# Binary search.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n          # left, right are the lowest and highest possible first bad versions

        while left < right:

            mid = (left + right) // 2
            if isBadVersion(mid):   # first bad version must be mid or before
                right = mid
            else:                   # first bad version must be after mid
                left = mid + 1

        return left