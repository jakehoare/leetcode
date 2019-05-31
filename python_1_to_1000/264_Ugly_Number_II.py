_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/ugly-number-ii/
# Write a program to find the n-th ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note that 1 is typically treated as an ugly number, and n does not exceed 1690.

# Create the sequence of ugly numbers and track the last index that has not been multiplied by 2 to generate another
# number in the sequence as i_2. Similarly track i_3 and i_5. The next number is the lowest new number that can be
# generated. Increment all indices that can generate thhe latest ugly number (since more than one of 2, 3 and 5 may be
# able to generate the last number.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        i_2, i_3, i_5 = 0, 0, 0     # last index in ugly of any not already be multiplied by 2, 3 and 5

        while len(ugly) < n:

            ugly.append(min(2 * ugly[i_2], 3 * ugly[i_3], 5 * ugly[i_5]))   # append smallest

            if ugly[-1] == 2 * ugly[i_2]:   # increment i_2 if latest ugly can be generated from 2 * ugly[i_2]
                i_2 += 1
            if ugly[-1] == 3 * ugly[i_3]:   # increment i_3 if latest ugly can be generated from 3 * ugly[i_3]
                i_3 += 1
            if ugly[-1] == 5 * ugly[i_5]:   # increment i_5 if latest ugly can be generated from 5 * ugly[i_5]
                i_5 += 1

        return ugly[-1]