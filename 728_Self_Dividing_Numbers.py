_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/self-dividing-numbers/
# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# Also, a self-dividing number is not allowed to contain the digit zero.
# Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds.

# Test each numbers. Repeatedly divide by 10 ro extract each digit, rejecting if original number is not divisible by
# digit or digit is zero.
# Time - O(n log k) where there are n numbers in range and k is the maximum number
# Space - O(n log n)

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        def is_self_dividing(num):

            copy = num              # make a copy since original num is also required

            while copy > 0:

                copy, digit = divmod(copy, 10)
                if digit == 0 or num % digit != 0:
                    return False

            return True

        return [num for num in range(left, right + 1) if is_self_dividing(num)]