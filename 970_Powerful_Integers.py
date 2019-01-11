_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/powerful-integers/
# Given two non-negative integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers
# i >= 0 and j >= 0.
# Return a list of all powerful integers that have value less than or equal to bound.
# You may return the answer in any order.  In your answer, each value should occur at most once.

# Create lists of all powers of x and y less than bound.
# Time - O((log b)**2) where b is the bound
# Space - O((log b)**2)

class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        result = set()

        def make_power_list(val):
            power_list = [1]
            if val != 1:            # val == 1 means list of only 1
                while power_list[-1] <= bound:
                    power_list.append(power_list[-1] * val)
                power_list.pop()    # last value is too large
            return power_list

        x_list, y_list = make_power_list(x), make_power_list(y)

        for x_num in x_list:
            for y_num in y_list:
                if x_num + y_num > bound:
                    break
                result.add(x_num + y_num)

        return list(result)