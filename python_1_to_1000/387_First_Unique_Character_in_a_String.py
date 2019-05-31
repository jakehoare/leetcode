_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/first-unique-character-in-a-string/
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Count frequency of each letter. Then iterate over s again, finding the index of the first letter with count of 1.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = [0 for _ in range(26)]

        for c in s:
            counts[ord(c) - ord("a")] += 1

        for i, c in enumerate(s):
            if counts[ord(c) - ord("a")] == 1:
                return i

        return -1