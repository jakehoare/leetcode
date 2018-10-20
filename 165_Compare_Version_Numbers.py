_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/compare-version-numbers/
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.

# Split by '.' and pad shorter list with [0]. Then compare each section.
# Time - O(n)
# Space - O(n)

import itertools

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(v) for v in version1.split('.')]                  # split by "." and convert to int
        v2 = [int(v) for v in version2.split('.')]

        for i1, i2 in itertools.zip_longest(v1, v2, fillvalue=0):   # pad shorter with zeros
            if i1 > i2:
                return 1
            if i1 < i2:
                return -1

        return 0            # all version components are same