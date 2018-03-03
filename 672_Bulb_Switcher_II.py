_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/bulb-switcher-ii/
# There is a room with n lights which are turned on initially and 4 buttons on the wall. After performing exactly m
# unknown operations towards buttons, you need to return how many different kinds of status of the n lights could be.
# Suppose n lights are labeled as number [1, 2, 3 ..., n], function of these 4 buttons are given below:
# Flip all the lights.
# Flip lights with even numbers.
# Flip lights with odd numbers.
# Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...

# In the general case of large m and n, we can apply amy of the 3 operations - even, odd, 3k + 1. This gives 2**3 = 8
# possible states. Additional m or  n do not lead to any more states. Smaller cases are considered individually.
# Time - O(1)
# Space - O(1)

class Solution(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if n == 0:
            return 0        # no lights
        if m == 0:
            return 1        # no switches

        if m == 1:          # one switch
            if n == 1:
                return 2    # off or on
            if n == 2:
                return 3    # not both on
            return 4        # evens, odds, every third or all off

        if m == 2:          # two switches
            if n == 1:
                return 2    # off or on
            if n == 2:
                return 4    # all possibilities
            if n >= 3:
                return 7    # all apart from on, on, off

        return 2 ** min(n, 3)  # any combination of evens, odds, every third