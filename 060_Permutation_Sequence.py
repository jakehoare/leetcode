_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/permutation-sequence/
# The set [1,2,3,…,n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, we get the following sequence (ie, for n = 3):
# "123", "132", "213", "231", "312", "321"
# Given n and k, return the kth permutation sequence.

# Find each digit according to the ratio between k and the total number of possible permutations.
# Time - O(n**2) since each iteration adds one digit and O9n) for del from list
# Space - O(n) to store chars list

from math import factorial

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        chars = [str(i) for i in range(1, n+1)]     # the symbols that will be permuted
        permutations = factorial(n)                 # total number of permutations for this n
        k -= 1                                      # change indexing to 0
        result = []

        while chars:
            digit = n * k // permutations           # get the first digit (range is 0 to n-1)
            result.append(chars[digit])             # map from digit to a symbol
            del chars[digit]                        # remove that symbol
            permutations //= n                      # repeat for next digit with decreased permutations, n and k
            k -= digit * permutations
            n -= 1

        return "".join(result)
