_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-segments-in-a-string/
# Count the number of segments in a string, where a segment is defined to be a contiguous sequence of
# non-space characters.

# Split by spaces.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
