_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/adding-two-negabinary-numbers/
# Given two numbers arr1 and arr2 in base -2, return the result of adding them together.
# Each number is given in array format:
# as an array of 0s and 1s, from most significant bit to least significant bit.
# For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.
# A number arr in array format is also guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.
# Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.

# Iterate over arrays from least to most significant digits.
# Add digits from both arrays to carry.
# If sum of digits and carry is 1 or 0, append that to result.
# If sum of digits and carry is 2, append 0, increment carry and next carry since 2**(n+2) - 2**(n+1) = 2*2**n.
# If sum of digits and carry is 3, append 1, increment carry and next carry since 2**(n+2) - 2**(n+1) = 2*2**n.
# If next carry is 1 and carry is 2 then these are netted to zero.

# Time - O(max(m, n))
# Space - O(max(m, n))

class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        carry, next_carry = 0, 0            # carry over to the following 2 digits
        result = []

        while arr1 or arr2 or carry or next_carry:
            digit = carry
            if arr1:
                digit += arr1.pop()
            if arr2:
                digit += arr2.pop()

            carry, next_carry = next_carry, 0
            result.append(digit % 2)
            if digit == 2 or digit == 3:
                carry += 1
            if digit >= 2:
                if carry >= 2:
                    carry -= 2
                else:
                    next_carry += 1

        while result[-1] == 0 and len(result) > 1:      # remove leading zeros
            result.pop()
        return result[::-1]                             # put most significant digit first
