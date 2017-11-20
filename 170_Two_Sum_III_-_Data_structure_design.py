_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/two-sum-iii-data-structure-design/
# Design and implement a TwoSum class. It should support the following operations: add and find.
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.

# Use a dictionary to store each number and whether it has been added multiple times.  To find, for each num in
# dictionary look for the difference between target value and that num, or for the num to be duplicated if it
# is half of the target value.
# Time - O(1) to add, O(n) to find
# Space - O(n)

class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.nums = {}      # key is num, value is True if num is duplicated else False

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.nums[number] = number in self.nums     # False for first occurence, True for multiple occurrences

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.nums:
            if value == 2 * num:        # need num to be duplicated
                if self.nums[num]:
                    return True
            else:                       # look for difference
                if value - num in self.nums:
                    return True
        return False

