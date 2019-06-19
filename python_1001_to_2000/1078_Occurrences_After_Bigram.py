_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/occurrences-after-bigram/
# Given words first and second, consider occurrences in some text of the form "first second third",
# where second comes immediately after first, and third comes immediately after second.
# For each such occurrence, add "third" to the answer, and return the answer.

# Split text by space and check for consecutive appearances of first and second.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        result = []
        s = text.split()

        for i in range(2, len(s)):
            if s[i - 2] == first and s[i - 1] == second:
                result.append(s[i])

        return result
