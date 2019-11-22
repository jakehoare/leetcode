_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/
# You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only.
# Your task is to make these two strings equal to each other.
# You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].
# Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

# Iterate along the strings together, flagging when s1 contains an additional x or y compared to s2.
# If we find an x in s1 and there is already an additional x, we can swap woth an additional y in s2.
# Similarly if there is a y in s1 and already an additional y.
# Fail if only x or y has an excess at the end, else perfoma a final double swap.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        s1_excess_x, s1_excess_y = False, False
        result = 0

        for c1, c2 in zip(s1, s2):
            if c1 == c2:
                continue

            if c1 == "x":
                if s1_excess_x:         # convert "xx" and "yy" to "xy" in both strings
                    result += 1
                s1_excess_x = not s1_excess_x   # toggle flag
            else:
                if s1_excess_y:
                    result += 1
                s1_excess_y = not s1_excess_y

        if s1_excess_x ^ s1_excess_y:   # cannot equalize if only x or y are in excess
            return -1
        return result + int(s1_excess_x) + int(s1_excess_y) # swap "xy" and "yx" to "xy" and "xy" in 2 moves