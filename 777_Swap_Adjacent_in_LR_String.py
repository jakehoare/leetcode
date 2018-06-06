_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/swap-adjacent-in-lr-string/
# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one
# occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR".
# Given the starting string start and the ending string end, return True if and only if there exists a sequence of
# moves to transform one string to the other.

# "L" can only move left and "R" can only move right. "L" and "R" cannot swap places. Maintain the net balance of "L"
# and "R" while iterating over both strings. If there are more "L" of fewer "R" then the first requirement is violated.
# If there is "R" in start and "L" in end then a swap is required. Final check for overall balance.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end):      # early return
            return False

        left, right = 0, 0              # net balance of "L" and "R" in start minus end

        for c1, c2 in zip(start, end):  # iterate over both strings together

            if c1 == "L":
                left += 1
            elif c1 == "R":
                right += 1

            if c2 == "L":
                left -= 1
            elif c2 == "R":
                right -= 1

            if left > 0 or right < 0:   # more "L" in start, cannot move right to reach those in end
                return False
            if left < 0 and right > 0:  # need to swap "L" and "R"
                return False

        return left == 0 and right == 0 # must be balanced
