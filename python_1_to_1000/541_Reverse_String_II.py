_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reverse-string-ii/
# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from
# the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k
# but greater than or equal to k characters, then reverse the first k characters and left the other as original.

# Iterate over s in steps of k.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        reverse = True
        result = []

        for i in range(0, len(s), k):
            block = s[i:i + k]
            if reverse:
                result.append(block[::-1])
            else:
                result.append(block)
            reverse = not reverse

        return "".join(result)