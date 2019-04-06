_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/
# Given a binary string S (a string consisting only of '0' and '1's) and a positive integer N,
# return true if and only if for every integer X from 1 to N, the binary representation of X is a substring of S.

# Brute force check of all numbers from N to 1. Check numbers in descending order because failure is more likely for
# large numbers than smaller numbers and if there is no solution we will return False sooner.
# The concatenation of the binary strings of all integers from 1 to N is of length O(N log N). If S is significantly
# shorter than this number then it is unlikely to be able to include all bit strings (despite the fact that some bit
# strings will overlap).
# Time - O(n log n)
# Space - O(log n)

class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        for num in range(N, 0, -1):
            if bin(num)[2:] not in S:       # ignore "0b" prefix of bin()
                return False

        return True
