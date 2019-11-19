_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/array-transformation/
# Given an initial array arr, every day you produce a new array using the array of the previous day.
# On the i-th day, you do the following operations on the array of day i-1 to produce the array of day i:
# If an element is smaller than both its left neighbor and its right neighbor, then this element is incremented.
# If an element is bigger than both its left neighbor and its right neighbor, then this element is decremented.
# The first and last elements never change.
# After some days, the array does not change. Return that final array.

# While the previous array was modified, decrement any peaks and increment any troughs.
# If any element was changed, update the flag so we check again until nothing is changed.
# Time - O(mn) for max value m of n elements
# Space - O(n)

class Solution(object):
    def transformArray(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        changed = True          # flag, true so we enter the while loop at least once

        while changed:
            new_arr = arr[:]
            changed = False     # reset
            for i in range(1, len(arr) - 1):
                if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                    new_arr[i] += 1
                    changed = True
                elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                    new_arr[i] -= 1
                    changed = True

            arr = new_arr

        return arr

