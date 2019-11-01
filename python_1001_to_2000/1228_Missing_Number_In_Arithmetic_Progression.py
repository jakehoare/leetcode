_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/missing-number-in-arithmetic-progression/
# In some array arr, the values were in arithmetic progression:
# the values arr[i+1] - arr[i] are all equal for every 0 <= i < arr.length - 1.
# Then, a value from arr was removed that was not the first or last value in the array.
# Return the removed value.

# If the first difference is twice the second difference, then the missing value should be second.
# Else if any difference is twice the first difference, the missing value is between the current values.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        first_diff = arr[1] - arr[0]
        if first_diff  == 2 * (arr[2] - arr[1]):
            return arr[0] + first_diff // 2

        for i in range(1, len(arr) - 1):
            if (arr[i + 1] - arr[i]) == first_diff * 2:
                return arr[i] + first_diff

