_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/next-greater-element-iii/
# Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same
# digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists,
# you need to return -1.

# Moving from right to left, find the first pair where n[left] < n[right]. Then moving right again, find the smallest
# digit that is more than n[left] and swap. Put all digits to the right of n[left] in increasing order.
# Time - O(log n), number of digits in n
# Space - O(1)

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = [c for c in str(n)]  # convert to list of chars

        i = len(num) - 1  # find num[i-1] < num[i], so swapping increases value
        while i > 0 and num[i - 1] >= num[i]:
            i -= 1

        if i == 0:  # no increase possible
            return -1

        j = i  # find lowest nums[j] that is > nums[i-1]
        while j + 1 < len(num) and num[j + 1] > num[i - 1]:
            j += 1

        num[j], num[i - 1] = num[i - 1], num[j]  # swap i-1 and j

        result = int("".join(num[:i] + sorted(num[i:])))  # sort after i
        # 2**31 - 1 is the largest signed 32 bit number
        return -1 if result >= 2 ** 31 else result
