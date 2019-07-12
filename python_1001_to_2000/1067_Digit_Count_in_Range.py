_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/digit-count-in-range/
# Given an integer d between 0 and 9, and two positive integers low and high as lower and upper bounds, respectively.
# Return the number of times that d occurs as a digit in all integers between low and high,
# including the bounds low and high.

# Helper function count_digits(n) recursively counts d in all integers less than n.
# Separate n into prefix (dividing by 0) and units (modulo 0).
# The 4 components to the count are:
# - fix prefix count d in units, provided d < units.
# - count of d in fixed prefix, followed by all units < d.
# - any int < prefix, followed by fixed d (not 0 prefix and 0 units).
# - result from prefix, followed by any digit 0 to 9.
# Time - O(log n)
# Space - O(log n)

class Solution(object):
    def digitsCount(self, d, low, high):
        """
        :type d: int
        :type low: int
        :type high: int
        :rtype: int
        """
        def count_digits(n):    # return count of d in integers less than n
            if n == 0 or (d == 0 and n <= 10):
                return 0

            result = 0
            prefix, units = divmod(n, 10)               # assume n = ppppu for prefix pppp and units u
            if units > d:                               # count the d in ppppd
                result += 1
            if prefix > 0:                              # count of d in prefix, followed by any units < d
                result += str(prefix).count(str(d)) * units
            result += prefix if d else prefix - 1       # any int < prefix, followed by d (exclude 0 then 0)
            result += count_digits(prefix) * 10         # count of any int < prefix, followed by any digit
            return result

        return count_digits(high + 1) - count_digits(low)
