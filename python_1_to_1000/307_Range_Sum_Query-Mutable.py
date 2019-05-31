_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/range-sum-query-mutable/
# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
# The update(i, val) function modifies nums by updating the element at index i to val.
# You may assume the number of calls to update and sumRange function is distributed evenly.

# Break nums into bins, each of size approx n**0.5 and containing approx n**0.5 nums.  Calculate the sum of each bin.
# To sumRange(), sum the bins from and including i to and excluding j, then add the sum of nums from the bin containing
# j and subtract the nums before i from the bin containing i.  Update nums as well as bin_sums.
# Alternatively calculate the running cumulative sums within each bin and of each bin, which makes O(n**0.5) to update
# and O(1) sumRange().
# Time - O(n) to initialise, O(1) to update, O(n**0.5) to sumRange().
# Space - O(n)

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.width = int(len(nums)**0.5)    # width of each bin (apart from last)
        self.bin_sums = []                  # sum of each bin
        self.nums = nums

        for i, num in enumerate(nums):
            if i % self.width == 0:         # start a new bin
                self.bin_sums.append(num)
            else:                           # add to last bin
                self.bin_sums[-1] += num


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        bin_i = i // self.width
        diff = val - self.nums[i]
        self.bin_sums[bin_i] += diff        # update bin_sums
        self.nums[i] = val                  # update nums


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        bin_i, bin_j = i // self.width, j // self.width
        range_sum = sum(self.bin_sums[bin_i:bin_j])         # sum of whole bins
        range_sum += sum(self.nums[bin_j*self.width:j+1])   # add partial last bin
        range_sum -= sum(self.nums[bin_i*self.width:i])     # subtract partial first bin
        return range_sum

