_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/compare-version-numbers/
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.

# Split by '.' and pad shorter list with [0].  Then compare each section.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = list(map(int, version1.split('.')))    # split by '.' and convert to int
        v2 = list(map(int, version2.split('.')))

        diff = len(v1) - len(v2)                    # pad shorter with [0]
        if diff > 0:
            v2.extend([0 for _ in range(diff)])
        else:
            v1.extend([0 for _ in range(-diff)])

        for i1, i2 in zip(v1, v2):
            if i1 > i2:
                return 1
            if i1 < i2:
                return -1

        return 0    # default is all same