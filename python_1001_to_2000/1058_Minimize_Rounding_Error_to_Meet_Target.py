_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimize-rounding-error-to-meet-target/
# Given an array of prices [p1,p2...,pn] and a target, round each price pi to Roundi(pi) so that the rounded array
# [Round1(p1),Round2(p2)...,Roundn(pn)] sums to the given target.
# Each operation Roundi(pi) could be either Floor(pi) or Ceil(pi).
# Return the string "-1" if the rounded array is impossible to sum to target.
# Otherwise, return the smallest rounding error, which is defined as Σ |Roundi(pi) - (pi)| for i from 1 to n,
# as a string with three places after the decimal.

# For each price, add the floor to the base and record the remaining decimal digits.
# If the target is below the base or above the total ceiling, return "-1".
# Sort the remainders then iterate along, rounding up the largest remainders until the target is reached.
# Round down all reaminders not rounded up and add to result.
# Time - O(n log n)
# Space - O(n)

class Solution(object):
    def minimizeError(self, prices, target):
        """
        :type prices: List[str]
        :type target: int
        :rtype: str
        """
        base = 0            # sum of price floors
        remainders = []     # decimal places, ints between 0 and 1000

        for price in prices:
            integer, remainder = price.split(".")
            base += int(integer)
            if remainder != "000":
                remainders.append(int(remainder))

        if target < base or target > base + len(remainders):
            return "-1"

        remainders.sort(reverse=True)
        result = 0
        i = 0

        while i < len(remainders) and base + i < target:
            result += 1000 - remainders[i]      # round up largest remainders first
            i += 1

        result += sum(remainders[i:])           # round down the rest of remainders
        return "{:.3f}".format(result / 1000)
