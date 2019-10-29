_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/stepping-numbers/
# A Stepping Number is an integer such that all of its adjacent digits have an absolute difference of exactly 1.
# For example, 321 is a Stepping Number while 421 is not.
# Given two integers low and high,
# find and return a sorted list of all the Stepping Numbers in the range [low, high] inclusive.

# Breadth-first search, starting with single digit integers.
# For each number in the frontier, reject if greater than high and add to result if greater than or equal to low.
# Extend the number with its final digit - 1 and final digit + 1, unless this would be < 0 or > 9.
# Repeat until there are no more numbers to extend.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def countSteppingNumbers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        result = []
        if low == 0:            # do not add zero unless low is 0, since we cannot start other integers with 0
            result.append(0)

        nums = [i for i in range(1, 10)]

        while nums:
            new_nums = []
            for num in nums:
                if num > high:
                    continue
                if num >= low:
                    result.append(num)
                last_digit = num % 10
                if last_digit != 0:
                    new_nums.append(num * 10 + last_digit - 1)
                if last_digit != 9:
                    new_nums.append(num * 10 + last_digit + 1)

            nums = new_nums

        return result

