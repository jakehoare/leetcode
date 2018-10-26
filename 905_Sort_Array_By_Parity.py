_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sort-array-by-parity/
# Given an array A of non-negative integers, return an array consisting of all the even elements of A,
# followed by all the odd elements of A.
# You may return any answer array that satisfies this condition

# Iterate over A, alternately adding elements to lists of elements at add and even indices. Concatenate result.
# In Pythonn the iteration is achieved by list comprehension.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return [num for num in A if num % 2 == 0] + [num for num in A if num % 2 == 1]