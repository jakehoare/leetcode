_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/palindrome-removal/
# Given an integer array arr, in one move you can select a palindromic subarray
# arr[i], arr[i+1], ..., arr[j] where i <= j, and remove that subarray from the given array.
# Note that after removing a subarray, the elements on the left and on the right of that subarray move
# to fill the gap left by the removal.
# Return the minimum number of moves needed to remove all numbers from the array.

# For each subarray there are 3 cases:
# 1) We can always remove each integer individually.
# 2) If the last 2 integers are the same, we can remove them together and then find the result from the remainder.
# 3) If any other integer is the same as the last integer, we can remove them and all the integers between for the same
# cost of removing all integers between.
# Time - O(n**3)
# Space - O(n**2)

class Solution(object):
    def minimumMoves(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        memo = {}   # memo[(i, j)] is the result for arr[i:j + 1]

        def dp(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            result = dp(i, j - 1) + 1  # remove each number individually

            if arr[j] == arr[j - 1]:
                result = min(result, dp(i, j - 2) + 1)

            for k in range(i, j - 1):
                if arr[j] == arr[k]:
                    # cost of dp(k + 1, j - 1) is the same as dp(k, j)
                    result = min(result, dp(i, k - 1) + dp(k + 1, j - 1))

            memo[(i, j)] = result
            return result

        return dp(0, len(arr) - 1)
