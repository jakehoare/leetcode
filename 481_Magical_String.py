_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/magical_string/
# A magical string S consists of only '1' and '2' and obeys the following rules:
# The string S is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string S itself.
# The first few elements of string S is the following: S = "1221121221221121122……"
# If we group the consecutive '1's and '2's in S, it will be: 1 22 11 2 1 22 1 22 11 2 11 22 ......
# and the occurrences of '1's or '2's in each group are: 1 2	2 1 1 2 1 2 2 1 2 2 ......
# You can see that the occurrence sequence above is the S itself.
# Given an integer N as input, return the number of '1's in the first N number in the magical string S.

# For each s[i], append to s i copies of a different digit from that currently at the end of s.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        i = 2  # next index to be processed
        s = [1, 2, 2]
        ones = 1

        while len(s) < n:

            digit = s[-1] ^ 3  # next digits(s) are different from previous end

            s.append(digit)
            if s[i] == 2:
                s.append(digit)

            if digit == 1:
                ones += s[i]

            i += 1

        if len(s) > n and s[-1] == 1:   # added too many ones
            ones -= 1
        return ones
