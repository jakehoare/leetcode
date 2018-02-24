_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/beautiful-arrangement-ii/
# Given two integers n and k, you need to construct a list which contains n different positive integers ranging from
# 1 to n and obeys the following requirement:
# Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|]
# has exactly k distinct integers.
# If there are multiple answers, print any of them.

# The criteria that there are k differences between consecutive numbers means those differences are 1, 2, .. k.
# Use the first k + 1 nums to produce a list with all the required differences. Build the list with the largest
# difference first, then taking numbers from each end in turn create all the other differences.
# Then append all the remaining nums in order (since any differences will already have been used).
# Time - O(n)
# Space - O(n)

class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        result = []
        low, high = 1, k + 1
        next_low = True

        while low <= high:
            if next_low:
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
            next_low = not next_low

        return result + list(range(k + 2, n + 1))

