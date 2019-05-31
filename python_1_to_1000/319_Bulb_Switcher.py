_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/bulb-switcher/
# There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb.
# On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith
# round, you toggle every i bulb. For the nth round, you only toggle the last bulb.
# Find how many bulbs are on after n rounds.

# The ith bulb is toggled twice by every pair a, b where a*b == i.  Thus every prime is toggled twice only, most
# bulbs are toggled an even number of times.  Only if i is a square then it has an odd number of divisors and is on.
# Time - O(1)
# Space - O(1)

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(n**0.5)
