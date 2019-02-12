_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/broken-calculator/
# On a broken calculator that has a number showing on its display, we can perform two operations:
# Double: Multiply the number on the display by 2, or;
# Decrement: Subtract 1 from the number on the display.
# Initially, the calculator is displaying the number X.
# Return the minimum number of operations needed to display the number Y.

# If X > Y then we never multiply, just repeatedly subtract 1.
# Otherwise reduce Y to X. Division reduces Y and addition increases Y.
# Greedily divide whenever possible, since it is optimal to divide a smaller number before adding, rather than add
# then divide a larger number.
# Time - O(log Y)
# Space - O(1)

class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        operations = 0

        while Y > X:
            operations += 1
            if Y % 2 == 0:
                Y //= 2
            else:
                Y += 1

        return X - Y + operations
