_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-absolute-difference/
# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute
# difference of any two elements.
# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr

# Sort the array and iterate along, calculating the difference between each pair.
# If the difference is less than the minimum distance, update the minimum and clear the previous results.
# Then if the difference is less than the minimum distance, append the pair to the results.
# Time - O(n log n)
# Space - O(n)

class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        results = []
        min_diff = float("inf")

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_diff:
                min_diff = diff
                results = []        # clear previous results

            if diff == min_diff:
                results.append([arr[i - 1], arr[i]])

        return results
