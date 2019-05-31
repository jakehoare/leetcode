_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/monotone-increasing-digits/
# Given a non-negative integer N, find the largest number that is less than or equal to N with monotone
# increasing digits. Recall that an integer has monotone increasing digits if and only if each pair of adjacent
# digits x and y satisfy x <= y.)

# Convert input to a list of integer digits. Iterate over digits. If next digit is lower than previous then move back
# along digits looking for a digit that can be decreased whilst maintaining monotone increasing overall. When found,
# decrease that digit and set all subsequent digits to 9 (max possible).
# Time - O(n)
# Space - O(n)

class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = [int(c) for c in str(N)]                    # make list of digits

        i = 0
        while i + 1 < len(s):

            if s[i + 1] < s[i]:                         # next digit is decreasing

                while i > 0 and s[i] - 1 < s[i - 1]:    # move back until s[i] can be decremented
                    i -= 1

                s[i] -= 1                               # decrement
                s[i + 1:] = [9] * (len(s) - i - 1)      # all else set to 9

                result = 0
                for val in s:
                    result = result * 10 + val
                return result

            else:
                i += 1

        return N                                        # N is monotone increasing