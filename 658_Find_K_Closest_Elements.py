_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-k-closest-elements/
# Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be
# sorted in ascending order. If there is a tie, the smaller elements are always preferred.

# Binary search for value closest to x, then expand outwards.
# Time - O(log n + k)
# Space - O(1)

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left, right = 0, len(arr) - 1  # region of search for x (inclusive)

        while left <= right:
            mid = (left + right) // 2
            if x == arr[mid]:
                left, right = mid, mid
                break
            elif x > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1

        else:  # find which of left and right is closer to x
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                right = left
            else:
                left = right

        while right - left + 1 < k:  # while result length less than k
            if right + 1 == len(arr) or abs(arr[left - 1] - x) <= abs(arr[right + 1] - x):  # add arr[left]
                left -= 1
            else:  # add arr[right]
                right += 1

        return arr[left:right + 1]