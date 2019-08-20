_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/
# Given a binary array data,
# return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.

# Count the number of ones.
# Iterate along the data with a sliding window of length of the number of ones.
# At each index, update the number of ones in the window.
# Update the result with the number of ones outside the window, that would have to move to group the ones together.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def minSwaps(self, data):
        """
        :type data: List[int]
        :rtype: int
        """
        ones = sum(data)
        window_sum = sum(data[:ones])       # initial sliding window
        result = ones - window_sum          # count of ones to move inside window

        for i in range(len(data) - ones):
            window_sum -= data[i]
            window_sum += data[i + ones]
            result = min(result, ones - window_sum)

        return result
