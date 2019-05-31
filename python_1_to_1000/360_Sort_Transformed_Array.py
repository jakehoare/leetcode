_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sort-transformed-array/
# Given a sorted array of integers nums and integer values a, b and c. Apply a function of the form f(x) = ax2 + bx + c
# to each element x in the array.  The returned array must be in sorted order.

# Shape of transformed function is U if a is positive.
# If a is +ve largest values are at ends.  Take largest and mve inwards, reverse final order.
# If a is -ve or zero then smallest values are at ends.  Take smallest and move inwards.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def transform(x):
            return a * x * x + b * x + c

        transformed = [transform(num) for num in nums]
        left, right = 0, len(nums) - 1
        result = []

        while left <= right:

            if (a > 0 and transformed[left] > transformed[right]) or (a <= 0 and transformed[right] > transformed[left]):
                result.append(transformed[left])
                left += 1
            else:
                result.append(transformed[right])
                right -= 1

        return result[::-1] if a > 0 else result

