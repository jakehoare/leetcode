_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
# Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from
# the multiplication table?
# Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return
# the k-th smallest number in this table.

# Binary search the range of possible answers, initially [1, m * n]. helper function determines whether there are at
# least k numbers in the multiplication table that are less than or equal to guess.
# Time - O(min(m, n) log(mn)
# Space - O(1)

class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        if m > n:                   # ensure m is smaller
            m, n = n, m

        def helper(guess):          # return True if there are at least k numbers in table <= guess
            count = 0
            for i in range(1, m + 1):
                temp = guess // i
                if temp > n:        # faster than count += min(n, guess // i)
                    count += n
                else:
                    count += temp
                if count >= k:      # stop iterating if count already too large
                    return True

            return False

        left, right = 1, m * n

        while left < right:

            mid = (left + right) // 2
            if helper(mid):
                right = mid
            else:
                left = mid + 1

        return left