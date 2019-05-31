_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/valid-perfect-square/
# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Binary search between 1 and num. Test if middle of earch region is the square root of num. If not, search region
# to left or right until solution or no more search region.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 1, num

        while left <= right:

            mid = (left + right) // 2
            square = mid * mid

            if square == num:
                return True

            if square > num:
                right = mid - 1
            else:
                left = mid + 1

        return False