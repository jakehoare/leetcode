_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/confusing-number/
# Given a number N, return true if and only if it is a confusing number, which satisfies the following condition:
# We can rotate digits by 180 degrees to form new digits.
# When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively.
# When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.
# A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.

# Iterate along the digits of S in reverse.
# If any digit cannot be rotated, return False. Else add the rotated digit to the result.
# Finally check if the result is different from the original number.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def confusingNumber(self, N):
        """
        :type N: int
        :rtype: bool
        """
        S = str(N)
        rotation = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        result = []

        for c in S[::-1]:  # iterate in reverse
            if c not in rotation:
                return False
            result.append(rotation[c])

        return "".join(result) != S
