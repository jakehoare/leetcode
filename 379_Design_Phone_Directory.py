_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/design-phone-directory/
# Design a Phone Directory which supports the following operations:
# get: Provide a number which is not assigned to anyone.
# check: Check if a number is available or not.
# release: Recycle or release a number.

# Store the set of all unused numbers.  Storing the used numbers does not allow finding a new number in O(1) time.
# Time - O(n) to initialise, O(1) all other operations
# Space - O(n)

class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        # need to find new numbers that are free, not numbers that are used
        # so only store the free set
        self.free = set(range(maxNumbers))

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        return self.free.pop() if self.free else -1

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number in self.free

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        self.free.add(number)