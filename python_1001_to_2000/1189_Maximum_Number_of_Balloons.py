_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-number-of-balloons/
# Given a string text, you want to use the characters of text to form as many instances
# of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Count the frequency of each letter.
# For each unique letter in "balloons", update the result with the minimum of the current result and the count of the
# letter in text divided by the count in "balloons".
# Time - O(n)
# Space - O(1)

from collections import Counter

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        counts = Counter(text)
        result = float("inf")

        for c, count in Counter("balloon").items():
            result = min(result, counts[c] // count)    # integer division

        return result
