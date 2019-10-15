_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/get-equal-substrings-within-budget/
# You are given two strings s and t of the same length.
# You want to change s to t.
# Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is,
# the absolute difference between the ASCII values of the characters.
# You are also given an integer maxCost.
# Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring
# of t with a cost less than or equal to maxCost.
# If there is no substring from s that can be changed to its corresponding substring from t, return 0.

# Maintain a sliding window of a substring with cost < maxCost.
# Iterate along the strings, adding the cost of changing the current character to the window cost.
# While the window cost is more than maxCost, remove characters from the front of the window.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        start = 0
        cost, result = 0, 0

        for i, (c1, c2) in enumerate(zip(s, t)):
            cost += abs(ord(c1) - ord(c2))
            while cost > maxCost:
                cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            result = max(result, i - start + 1)

        return result
