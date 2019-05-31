_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/complex-number-multiplication/
# Given two strings representing two complex numbers.
# You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

# Split by "+" into real and imaginary.
# Time - O(max(m, n))
# Space - O(max(m , n))

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_real, a_im = a.split("+")
        a_real, a_im = int(a_real), int(a_im[:-1])

        b_real, b_im = b.split("+")
        b_real, b_im = int(b_real), int(b_im[:-1])

        c_real = a_real * b_real - a_im * b_im
        c_im = a_real * b_im + a_im * b_real

        return str(c_real) + "+" + str(c_im) + "i"
