_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/string-transforms-into-another-string/
# Given two strings str1 and str2 of the same length,
# determine whether you can transform str1 into str2 by doing zero or more conversions.
# In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.
# Return true if and only if you can transform str1 into str2.

# If the stings are not identical and str2 uses all 26 possible characters, then changing any character of str1
# would make it the same as some other character in str2, which means we cannot perform the transformation.
# Else find all indices in str1 of each char. Find the chars in str2 at the indices of each char in str1.
# If a char of str1 maps to more than one char of str2,
# then we cannot transform it into those 2 or more different chars.
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def canConvert(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        if len(set(str2)) == 26 and str1 != str2:
            return False

        char1_indices = defaultdict(list)
        for i, c in enumerate(str1):
            char1_indices[c].append(i)

        for c, indices in char1_indices.items():
            if len({str2[i] for i in indices}) != 1:
                return False

        return True
