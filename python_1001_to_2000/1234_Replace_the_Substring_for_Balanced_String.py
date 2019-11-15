_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/replace-the-substring-for-balanced-string/
# You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.
# A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.
# Return the minimum length of the substring that can be replaced with any other string of the same
# length to make the original string s balanced.
# Return 0 if the string is already balanced.

# For each char of s, count the excess chars above the balanced expectation (n / 4).
# Then iterate over s.
# If a char has an excess count, decrement the excess count since it is now in the replacement substring.
# If/while there are no excess chars, update the result, move the start of the subtring forwards and increment any
# excess chars that are no longer in the substring.
# Time - O(n), since to check all values of excess is O(1) because it has at most 26 elements.
# Space - O(1)

from collections import Counter

class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        balance = len(s) // 4
        excess = {}
        for c, count in Counter(s).items():
            if count - balance > 0:
                excess[c] = count - balance
        if not excess:
            return 0

        start = 0
        result = len(s)

        for end, c in enumerate(s):
            if c in excess:
                excess[c] -= 1
            while all(v <= 0 for v in excess.values()):
                result = min(result, end - start + 1)
                if s[start] in excess:
                    excess[s[start]] += 1
                start += 1

        return result
