_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/additive-number/
# Additive number is a string whose digits can form additive sequence.  A valid additive sequence should contain at
# least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of
# the preceding two.

# Try all possible starting digit pairs with lengths such that the remainder has at least as many digits as the
# longer of the 2 starting digits.  Break out of loop if any number begins with 0 and has length > 1.
# For each starting pair, repeatedly add the last 2 numbers and check if this is equal to the next number until end.
# Time - O(n**3)
# Space - O(1)

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        if n < 3:
            return False

        for second in range(1, 1 + (n - 1) // 2):       # first digit of second integer
            if num[0] == "0" and second > 1:
                break
            third = second + 1                          # first digit of third integer

            while n - third >= max(second, third - second):
                if num[second] == "0" and third > second + 1:
                    break

                n1, n2 = int(num[0:second]), int(num[second:third])
                start = third
                while True:
                    next_int = n1 + n2
                    next_start = start + len(str(next_int))
                    if num[start] == "0" and next_start > start + 1:
                        break
                    if next_int != int(num[start:next_start]):
                        break
                    if next_start == n:
                        return True
                    n1, n2, start = n2, next_int, next_start

                third += 1

        return False
