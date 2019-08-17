_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-of-absolute-value-expression/
# Given two arrays of integers with equal lengths, return the maximum value of:
# |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
# where the maximum is taken over all 0 <= i, j < arr1.length.

# Each of arr1[i], arr2[i] and i can be positive or negative.
# So there are 2**3 == 8 ways to combine those three values.
# Some combinations are the negative of other, so there are actually 4 ways ignoring sign.
# Calculate the 4 ways, then return the maximum of the greatest range of each way.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        temp1, temp2, temp3, temp4 = [], [], [], []
        for i, (a1, a2) in enumerate(zip(arr1, arr2)):
            temp1.append(a1 + a2 + i)
            temp2.append(a1 + a2 - i)
            temp3.append(a1 - a2 + i)
            temp4.append(a1 - a2 - i)

        return max(max(temp) - min(temp) for temp in [temp1, temp2, temp3, temp4])
