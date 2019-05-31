_author_ = 'jake'
_project_ = 'leetcode'


# https://leetcode.com/problems/contiguous-array/
# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Store in dictionary net balance of 1s and 0s for every prefix array. Search for same net balance.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        balance = 0         # net 1s - 0s
        balances = {0: -1}  # key is balance, value is index

        for i, num in enumerate(nums):

            if num == 1:
                balance += 1
            else:
                balance -= 1

            if balance in balances:
                max_len = max(max_len, i - balances[balance])
            else:
                balances[balance] = i

        return max_len
