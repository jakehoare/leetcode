_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/custom-sort-string/
# S and T are strings composed of lowercase letters. In S, no letter occurs more than once.
# S was sorted in some custom order previously. We want to permute the characters of T so that they match the order
# that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.
# Return any permutation of T (as a string) that satisfies this property.

# Count the frequencies of all letters in T. For each letter in S, add to the result the number of copies of the letter
# in T. Finally add all copies of lteers in T that are not in S.
# Time - O(m + n)
# Space - O(m)

from collections import Counter

class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        result = []
        t_count = Counter(T)

        for c in S:
            result += [c] * t_count[c]      # do not create strings with c * t_count[c]
            del t_count[c]

        for c, count in t_count.items():
            result += [c] * count
        return "".join(result)
