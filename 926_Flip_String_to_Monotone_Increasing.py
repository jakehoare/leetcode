_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/flip-string-to-monotone-increasing/
# A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0),
# followed by some number of '1's (also possibly 0.)
# We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.
# Return the minimum number of flips to make S monotone increasing.

# To make monotone increasing, there is one point in S where all chars on the left are 0 and all on the right are 1.
# Count the zeros. Initial case is to flip all zeros to ones.
# For each char, if zero then decrement the number of zeros to be flipped (since the zero is then on the left).
# If one, then increment the number of ones to be flipped.
# Time - O(n)
# Space - O(1)

class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        zeros, ones = S.count("0"), 0
        result = zeros

        for c in S:

            if c == "0":
                zeros -= 1
            else:
                ones += 1

            result = min(result, zeros + ones)

        return result