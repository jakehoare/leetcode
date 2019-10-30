_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/confusing-number-ii/
# We can rotate digits by 180 degrees to form new digits.
# When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively.
# When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.
# A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.
# Note that the rotated number can be greater than the original number.
# Given a positive integer N, return the number of confusing numbers between 1 and N inclusive.

# Helper function take a number and its rotation and updates count for number and all greater confusing numbers <= N.
# Update result if confusing, then recurse for all 5 valid digits appended to number.
# Time - O(5 ** log n), where log is base 10
# Space - O(5 ** log n)

class Solution(object):
    def confusingNumberII(self, N):
        """
        :type N: int
        :rtype: int
        """
        valid = [0, 1, 6, 8, 9]
        rotations = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

        self.count = 0

        def helper(num, rotation):
            length = len(str(num))
            if num != rotation:
                self.count += 1
            for i in valid:
                if num * 10 + i > N:
                    return
                helper(num * 10 + i, rotations[i] * 10 ** length + rotation)

        for num in valid[1:]:       # do not start with zero
            helper(num, rotations[num])

        return self.count
