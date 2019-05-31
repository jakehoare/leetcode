_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/string-without-aaa-or-bbb/
# Given two integers A and B, return any string S such that:
# S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
# The substring 'aaa' does not occur in S;
# The substring 'bbb' does not occur in S.

# If A and B are not equal, create as many groups of "xxy" as possible where x is the letter with the greater count.
# Each group reduces the count difference by 1. Then add as many pairs of "ab" as possible, followed by any
# remaining single letters.
# Time - O(a + b)
# Space - O(a + b)

class Solution:
    def strWithout3a3b(self, a, b):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        result = []
        diff = a - b
        if diff > 0:
            groups = min(diff, b)
            result = ["aab"] * groups       # equalize the difference as much as possible
            a -= 2 * groups                 # update remaining required letters
            b -= groups
        elif diff < 0:
            groups = min(-diff, a)
            result = ["bba"] * groups
            b -= 2 * groups
            a -= groups

        pairs = min(a, b)
        result += ["ab"] * pairs
        a -= pairs
        b -= pairs

        result += ["a"] * a + ["b"] * b     # at most one of "a" or "b"

        return "".join(result)
