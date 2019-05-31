_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/rotated-digits/
# X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different
# from X.  Each digit must be rotated - we cannot choose to leave it alone.
# A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to
# each other; 6 and 9 rotate to each other, the rest of the numbers do not rotate to any other number.
# Now given a positive number N, how many numbers X from 1 to N are good?

# Test each integer. If any digit cannot be rotated then integer is not good. Also if integer does not contain at least
# one digit that is different after rotation, it is bad.
# Time - O(n log n) since each integer has O(log n) digits.
# Space - O(log n)

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        bad = {"3", "4", "7"}
        opposites = {"2", "5", "6", "9"}

        for i in range(1, N + 1):

            digits = set(str(i))
            if not bad.intersection(digits) and opposites.intersection(digits):
                count += 1

        return count
