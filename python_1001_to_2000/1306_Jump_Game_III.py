_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/jump-game-iii/
# Given an array of non-negative integers arr, you are initially positioned at start index of the array.
# When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.
# Notice that you can not jump outside of the array at any time.

# Recursive helper returns False if index is outside array and True if value is zero.
# Else recurse jumping by +/- arr[i].
# Record visited indices to avois loops.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        n = len(arr)
        visited = set()

        def helper(i):
            if i < 0 or i >= n:
                return False
            if arr[i] == 0:
                return True
            if i in visited:
                return False
            visited.add(i)

            return helper(i + arr[i]) or helper(i - arr[i])

        return helper(start)
