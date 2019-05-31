_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
# In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
# Return the element repeated N times.

# Iterate over A, adding elements to set. Return when duplicated element is found.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        seen = set()

        for num in A:
            if num in seen:
                return num
            seen.add(num)
