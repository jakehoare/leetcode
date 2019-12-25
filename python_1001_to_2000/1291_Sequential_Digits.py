_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sequential-digits/
# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

# Starting from the digits from 1 to 9, extend each number by the next greater digit.
# If a number is more than high, return the result since all later numbers are greater.
# If a number is greater than or equal to low, append it to the result.
# Time - O(log n)
# Space - O(log n)

class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        nums = list(range(1, 10))
        result = []

        while nums:
            new_nums = []

            for num in nums:
                if num > high:
                    break
                if num >= low:
                    result.append(num)
                last_digit = num % 10
                if last_digit != 9:     # extend with next greater digit
                    new_nums.append(num * 10 + last_digit + 1)

            nums = new_nums

        return result
