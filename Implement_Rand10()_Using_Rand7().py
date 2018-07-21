_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/implement-rand10-using-rand7/
# Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which
# generates a uniform random integer in the range 1 to 10.

# Create a 2 digit number in base 7, of which there are 49. Use only the first 40, where the units in base 10 have
# an equal probability of being each digit.
# Time - O(infinity), expected is sum of arithmetico–geometric sequence
# Space - O(1)

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        units = rand7() - 1
        sevens = rand7() - 1
        num = 7 * sevens + units    # between 0 and 48 inclusive

        if num >= 40:               # use on 0 to 39 inclusive
            return self.rand10()

        return (num % 10) + 1       # take units digit