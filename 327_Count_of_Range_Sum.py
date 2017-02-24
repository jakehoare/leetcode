_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/count-of-range-sum/
# Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
# Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

# Create an array of the cumulative prefix sums.  Mergesort this array, counting the number of range sums purely
# within LHS and RHS.  Then given that both sides are sorted, for each prefix_sum in LHS find the indices i and j
# that define the ranges summing to between lower and upper.  Perform the merge using python sorted().
# Time - O(n log n)
# Space - O(n)

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        cumul = [0]
        for num in nums:
            cumul.append(num + cumul[-1])

        def mergesort(cumul, left, right):      # sorting cumul[left:right]
            count = 0
            if right - left <= 1:
                return count

            mid = (left + right) // 2
            count += mergesort(cumul, left, mid) + mergesort(cumul, mid, right)     # range counts within both sides
            i, j = mid, mid
            for prefix_sum in cumul[left:mid]:                      # range count across mid
                while i < right and cumul[i] - prefix_sum < lower:  # find first index in RHS that sums >= lower
                    i += 1
                while j < right and cumul[j] - prefix_sum <= upper: # find last index in RHS that sums > upper
                    j += 1
                count += (j - i)    # for next prefix_sum, restart at i and j since they can only increase

            cumul[left:right] = sorted(cumul[left:right])   # merge
            return count

        return mergesort(cumul, 0, len(cumul))

