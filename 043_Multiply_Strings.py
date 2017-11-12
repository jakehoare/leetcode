_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/multiply-strings/
# Given two numbers represented as strings, return multiplication of the numbers as a string.
# The numbers can be arbitrarily large and are non-negative.
# Converting the input string to integer is NOT allowed.
# You should NOT use internal library such as BigInteger.

# Create a list of each digit in the result, starting wiht the least significant digit.
# Reverse input digit order. nums1[i] * nums2[j] is added to result[i+j+1] and result[i+j]
# Alternatively: return str(int(num1) * int(num2))
# Time - O(m * n) where inputs are of lengths m and n
# Space - O(max(m,n))

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]         # easier to work with lowest digits first
        result = [0] * (len(num1) + len(num2))


        for i in range(len(num1)):

            int1 = ord(num1[i]) - ord('0')

            for j in range(len(num2)):

                int2 = ord(num2[j]) - ord('0')

                tens, units = divmod(int1 * int2, 10)

                result[i + j] += units      # add units and handle carry of units
                if result[i + j] > 9:
                    result[i + j + 1] += result[i + j] // 10
                    result[i + j] %= 10

                result[i + j + 1] += tens   # add tens and handle carry of tens
                if result[i + j + 1] > 9:
                    result[i + j + 2] += result[i + j + 1] // 10
                    result[i + j + 1] %= 10

        while len(result) > 1 and result[-1] == 0:  # remove trailing zeros
            result.pop()
        return "".join(map(str, result[::-1]))      # reverse and convert to string

